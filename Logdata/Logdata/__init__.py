import os
from flask import Flask, render_template, request, url_for

from Logdata.Database import DBManager


def print_settings(config):
    print('========================================================')
    print('SETTINGS for Log Data for Android APPLICATION')
    print('========================================================')
    for key, value in config:
        print('%s=%s' % (key, value))
    print('========================================================')


def not_found(error):
    return render_template('404.html'), 404


def server_error(error):
    err_msg = str(error)
    return render_template('500.html', err_msg=err_msg), 500


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


def create_app(config_filepath='resource/config.cfg'):
    log_data_app = Flask(__name__)

    from Logdata.Log_Data_Config import LogDataAndroidConfig
    log_data_app.config.from_object(LogDataAndroidConfig)
    log_data_app.config.from_pyfile(config_filepath, silent=True)
    print_settings(log_data_app.config.items())

    # 로그 초기화
    from Logdata.Log_Data_Logger import Log
    log_filepath = os.path.join(log_data_app.root_path, log_data_app.config['LOG_FILE_PATH'])
    Log.init(log_filepath=log_filepath)

    # 뷰 함수 모듈은 어플리케이션 객체 생성하고 블루프린트 등록전에
    # 뷰 함수가 있는 모듈을 임포트해야 해당 뷰 함수들을 인식할 수 있음
    from Logdata.controller import LogDataController
    from Logdata.controller import CrashController
    from Logdata.controller import MainController
    from Logdata.Log_Data_Blueprint import logdata
    log_data_app.register_blueprint(logdata)

    # 공통으로 적용할 HTTP 404과 500 에러 핸들러를 설정
    log_data_app.error_handler_spec[None][404] = not_found
    log_data_app.error_handler_spec[None][500] = server_error

    # 페이징 처리를 위한 템플릿 함수
    log_data_app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    log_data_app.jinja_env.auto_reload = True
    log_data_app.config['TEMPLATES_AUTO_RELOAD'] = True

    # 데이터베이스 초기화
    log_data_app.config['MONGODB_SETTINGS'] = {'db': ['logdata_android', 'crashdata_android']}
    DBManager.init(log_data_app)

    return log_data_app
