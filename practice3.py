from flask import Flask

app = Flask(__name__)
@app.route('/main/<user_name>')

def Login(user_name):
    return 'Hello, ' + user_name

@app.route('/id/<int:message_id>')
def Logout(message_id):
    return 'message : %d' % message_id

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = '8080')