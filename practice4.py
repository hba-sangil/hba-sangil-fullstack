from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')
@app.route('/html_test')

def hello_html():
    var1 = 54
    return render_template('practice3.html', values = var1)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = '8080')