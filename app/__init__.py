from flask import Flask, jsonify
from flask_restful import Api
from flask_restful.utils import cors


from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.firestore import db
from app.users.api_v1_0.resources import users_v1_0_bp


def create_app():
    app = Flask(__name__)

    # Capture all 404 errors
    api = Api(app, catch_all_404s=True)
    api.decorators = [cors.crossdomain(origin='*')]

    # Disable strict mode when URL ends with /
    app.url_map.strict_slashes = False

    # Register blueprints
    app.register_blueprint(users_v1_0_bp)

    # Register personalized error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': 'Internal server error'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404
