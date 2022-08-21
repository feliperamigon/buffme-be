from flask import jsonify, Blueprint
from flask_restful import Api, Resource
import json
import requests as r
from config.settings import TRN_API_KEY, PUBLIC_TRN_URL
from ..models import User

# Functions
from ...firestore import insert_user

URL_HEADERS = {'TRN-Api-Key': TRN_API_KEY}

users_v1_0_bp = Blueprint('users_v1_0_bp', __name__)

api = Api(users_v1_0_bp)


class ProfileResource(Resource):
    def get(self, profile_user_identifier):
        profile_url = PUBLIC_TRN_URL + profile_user_identifier
        response = r.get(url=profile_url, params=URL_HEADERS)
        resp_dict = json.loads(response.content)
        user_info = resp_dict['data']['platformInfo']
        new_user = User(user_info['avatarUrl'], user_info['platformSlug'], user_info['platformUserHandle'],
                        user_info['platformUserId'])
        insert_user(dict(new_user))


class StatsResource(Resource):
    def get(self, profile_user_identifier, segment_type):
        stats_url = PUBLIC_TRN_URL + profile_user_identifier + '/segments/' + segment_type
        data = r.get(url=stats_url, params=URL_HEADERS).json()
        return jsonify({'controllers': data})


class PingResource(Resource):
    def get(self):
        return '', 204


api.add_resource(ProfileResource, '/api/profile/<string:profile_user_identifier>')
api.add_resource(StatsResource, '/api/stats/<string:profile_user_identifier>/<string:segment_type>')
api.add_resource(PingResource, '/ping')
