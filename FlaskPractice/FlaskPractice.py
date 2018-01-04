from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/logdata', methods=['GET', 'POST'])
def logData():
    if request.method == 'GET':
        print("request get")
        return "request get"
    elif request.method == 'POST':
        print("request post")
        print(request.content_type)
        print(request.form)
        print(request.data)
        return "request post"
    else:
        return 'Hello Logdata'
    # return request.data


@app.route('/crash', methods=['POST'])
def crash():
    print(request.data)
    print(request.form)
    print('crash')
    return str(request.form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
