from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods = ["GET", "POST", "PUT", "DELETE"])
def test():
    if request.method == "POST":
        print('POST')
        data = request.get_json()   ##API 리턴값은 flask의 jsonify함수를 이용해서 json형식으로 리턴값을 넣어준다.
        print(data['email'])
        
    if request.method == "GET":
        print('GET')
        data = request.args.get('email')
        print()
        
    if request.method == "PUT":
        print('PUT')
        user = request.args.get('email')
        print(user)
        
    if request.method == "DELETE":
        print('DELETE')
        user = request.args.get('email')
        print(user)
    return make_response(jsonify({'status' : True}), 200)

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = '8080')