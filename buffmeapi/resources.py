from flask import jsonify
from flask_restful import Resource
import requests as r
from buffmeapi.settings import TRN_API_KEY, PUBLIC_TRN_URL

# Models
from buffmeapi.models import User
import json
from json import JSONDecodeError

# Functions
import buffmeapi.profile as fs_profile

URL_HEADERS = {'TRN-Api-Key': TRN_API_KEY}


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