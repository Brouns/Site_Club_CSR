from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='site_bootstrap/templates')

@app.route('/')
def index():
    return render_template('index.html', title='Club de Sciences et Robotique')

@app.route('/about')
def about():
    return render_template('about.html', title='à propos de nous')

@app.route('/news')
def news():
    return render_template('news.html', title='newsletter')

@app.route('/infos')
def infos():
    return render_template('infos.html', title='infos pratiques')

@app.route('/contact')
def contact():
    return render_template('contact.html', title = 'contact')

if __name__ == '__main__':
    app.run()