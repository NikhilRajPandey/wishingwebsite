# Install flask if you have not installed
# It will takes one ports
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/wish')
def username():
    if request.args.get('submit', 'Submit'):
        usr = request.args.get('username', '')
        url = request.url
        recv = request.args.get('reciver','')
        return render_template('wish.html',usrname=usr,recv=recv,url=url)

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
# for get request link at http://flask.pocoo.org/docs/1.0/quickstart/#the-request-object
'''
I have research everywhere but i have found the get request code at ^ link
'''
app.run()