from flask import Flask, jsonify
from flask_restful import Resource, Api
import requests as r

#Creating the flask app
app = Flask(__name__)

#Creating an API Object
api = Api(app)

TRN_API_KEY = 'fd75b598-5e7f-4de9-a6ba-f3e39f918876'
class Home(Resource):

    def get(self):
        return jsonify({'message': 'Buffme Flask API!'})

class Profile(Resource):

    def get(self, profile_user_identifier):
        PROFILE_URL='https://public-api.tracker.gg/v2/csgo/standard/profile/steam/' + profile_user_identifier
        params = {'TRN-Api-Key': TRN_API_KEY}
        data = r.get(url = PROFILE_URL, params = params).json()
        return jsonify({'data': data})

class Stats(Resource):
    def get(self, profile_user_identifier, segment_type):
        PROFILE_URL='https://public-api.tracker.gg/v2/csgo/standard/profile/steam/' + profile_user_identifier + '/segments/' + segment_type
        params = {'TRN-Api-Key': TRN_API_KEY}
        data = r.get(url = PROFILE_URL, params = params).json()
        return jsonify({'data': data})


#adding the defined resources along with their corresponding urls
api.add_resource(Home, '/')
api.add_resource(Profile, '/profile/<string:profile_user_identifier>')
api.add_resource(Stats, '/stats/<string:profile_user_identifier>/<string:segment_type>')


if __name__ == '__main__':
    app.run()
