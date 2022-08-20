from flask import Flask
from flask_restful import Api

from api.resources import Home, Profile, Stats

#Creating the flask app
app = Flask(__name__)

#Creating an API Object
api = Api(app)

#adding the defined resources along with their corresponding urls
api.add_resource(Home, '/')
api.add_resource(Profile, '/profile/<string:profile_user_identifier>')
api.add_resource(Stats, '/stats/<string:profile_user_identifier>/<string:segment_type>')


if __name__ == '__main__':
    app.run()
