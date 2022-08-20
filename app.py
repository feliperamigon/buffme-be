from flask import Flask
from flask_restful import Api

import resources

# Creating the flask app
app = Flask(__name__)

# Creating an API Object
api = Api(app)


# Default routes

@app.route('/ping')
def ping():
    return '', 204

# Adding the defined resources along with their corresponding urls

app.register_blueprint()

api.add_resource(resources.Home, '/')
api.add_resource(resources.Profile, '/profile/<string:profile_user_identifier>')
api.add_resource(resources.Stats, '/stats/<string:profile_user_identifier>/<string:segment_type>')

if __name__ == '__main__':
    app.run()
