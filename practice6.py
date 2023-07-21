from flask import Flask, render_template, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/test", methods=['GET'])
def practice():
    return make_response(jsonify(success=True), 200)

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = '8080')