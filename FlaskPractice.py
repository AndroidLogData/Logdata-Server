from flask import request

from FlaskPractice import create_app

app = create_app()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/crash', methods=['POST'])
def crash():
    print(request.data)
    print(request.form)
    print('crash')
    return str(request.form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
