from flask import jsonify, Blueprint
from flask_restful import Api, Resource
import json
import requests as r
from config.settings import TRN_API_KEY, PUBLIC_TRN_URL
from ..models import User, Stats

# Functions
from ...firestore import get_user, get_map_stats, get_weapon_stats

URL_HEADERS = {'TRN-Api-Key': TRN_API_KEY}

users_v1_0_bp = Blueprint('users_v1_0_bp', __name__)

api = Api(users_v1_0_bp)


class ProfileResource(Resource):
    def get(self, profile_user_identifier):
        profile_url = PUBLIC_TRN_URL + profile_user_identifier
        response = r.get(url=profile_url, params=URL_HEADERS)
        if response.status_code == 200:
            resp_dict = json.loads(response.content)
            user_info = resp_dict['data']['platformInfo']
            lifetime_stats_overview = resp_dict['data']['segments'][0]
            user = User(user_info['avatarUrl'],
                        user_info['platformSlug'],
                        user_info['platformUserHandle'],
                        user_info['platformUserId'],
                        lifetime_stats_overview['stats']
                        )
            firestore_res = get_user(dict(user))
            return jsonify(firestore_res)
        elif response.status_code == 451:
            return jsonify({
                'type': 'Server Error',
                'message': 'The player either has not played CSGO or their profile is private.',
                'status': response.status_code
            })


class StatsResource(Resource):
    def get(self, profile_user_identifier, segment_type):
        stats_url = PUBLIC_TRN_URL + profile_user_identifier + '/segments/' + segment_type
        response = r.get(url=stats_url, params=URL_HEADERS)
        if response.status_code == 200:
            resp_dict = json.loads(response.content)
            stats_info = resp_dict
            stats = Stats(profile_user_identifier, stats_info)
            firestore_res = get_map_stats(dict(stats)) if segment_type == 'map' else get_weapon_stats(dict(stats))
            return jsonify(firestore_res)
        elif response.status_code == 451:
            return jsonify({
                'type': 'Server Error',
                'message': 'The player either has not played CSGO or their profile is private.',
                'status': response.status_code
            })


class PingResource(Resource):
    def get(self):
        return '', 204


api.add_resource(ProfileResource, '/api/profile/<string:profile_user_identifier>')
api.add_resource(StatsResource, '/api/stats/<string:profile_user_identifier>/<string:segment_type>')
api.add_resource(PingResource, '/ping')
