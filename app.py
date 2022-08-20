from flask import Flask, jsonify
from flask_restful import Api, Resource
import requests as r
from api.settings import TRN_API_KEY, PUBLIC_TRN_URL

# Models
from api.models import User
import json
from json import JSONDecodeError

# Functions
import functions.functions.profile as fs_profile


URL_HEADERS = {'TRN-Api-Key': TRN_API_KEY}

# Creating the flask app
app = Flask(__name__)

# Creating an API Object
api = Api(app)

# Resources
class Home(Resource):

    def get(self):
        return jsonify({'message': 'Buffme Flask API!'})

class Profile(Resource):

    def get(self, profile_user_identifier):
        PROFILE_URL= PUBLIC_TRN_URL + profile_user_identifier
        response = r.get(url = PROFILE_URL, params = URL_HEADERS)
        try:
            resp_dict = json.loads(response.content)
            user_info = resp_dict['data']['platformInfo']
            new_user = User(user_info['avatarUrl'], user_info['platformSlug'], user_info['platformUserHandle'], user_info['platformUserId'])
            fs_profile.insert_user(dict(new_user))
            print('Profile has been saved.')
        except JSONDecodeError:
            print('Profile data could not be serialized')

class Stats(Resource):

    def get(self, profile_user_identifier, segment_type):
        STATS_URL= PUBLIC_TRN_URL + profile_user_identifier + '/segments/' + segment_type
        data = r.get(url = STATS_URL, params = URL_HEADERS).json()
        return jsonify({'data': data})

# Adding the defined resources along with their corresponding urls
api.add_resource(Home, '/')
api.add_resource(Profile, '/profile/<string:profile_user_identifier>')
api.add_resource(Stats, '/stats/<string:profile_user_identifier>/<string:segment_type>')


if __name__ == '__main__':
    app.run()
