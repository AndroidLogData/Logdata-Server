from flask import Flask

from FlaskPractice.database import DBManager


def create_app(config_filepath='resource/config.cfg'):
    flask_practice = Flask(__name__)
    flask_practice.config['MONGODB_SETTINGS'] = {'db': 'logdata_android'}

    from FlaskPractice.controller import LogDataViewer

    from FlaskPractice.FlackPractice_blueprint import flaskPractice
    flask_practice.register_blueprint(flaskPractice)

    DBManager.init(flask_practice)

    return flask_practice
