from flask import Flask
from flask import render_template
from flask import current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    render_template('about.html')


if __name__ == '__main__':
    app.run()