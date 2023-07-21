from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')
@app.route('/doosan')

def practice():
    return render_template('blog_A.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080')