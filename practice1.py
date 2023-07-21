from flask import Flask

app = Flask(__name__)
@app.route('/hello')
def hello():
    return '<h1>Hello World</h1>'

@app.route('/hello/greet')
def greet():
    return '<h2>My name is ParkSangil</h2>'

@app.route('/hello/job')
def job():
    return '<h3>My job is student</h3>'

#동적 URL 다루기
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'hello, {user_name}({user_id})!'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = '8080')