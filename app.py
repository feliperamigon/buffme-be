from flask import Flask
from flask_restful import Api

from modules import MODULES_BLUEPRINT
from functions import FUNCTIONS_BLUEPRINT

from modules.resources import Home, Profile, Stats

# Creating the flask app
app = Flask(__name__)

# Creating an API Object
api = Api(app)

# Register blueprints
app.register_blueprint(MODULES_BLUEPRINT)
app.register_blueprint(FUNCTIONS_BLUEPRINT)

# Adding the defined resources along with their corresponding urls
api.add_resource(Home, '/')
api.add_resource(Profile, '/profile/<string:profile_user_identifier>')
api.add_resource(Stats, '/stats/<string:profile_user_identifier>/<string:segment_type>')


if __name__ == '__main__':
    app.run()
