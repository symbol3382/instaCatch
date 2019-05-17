from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from Followers import Followers

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_login', methods=['POST'])
def check_login():
    if request.method == 'POST':
        followers = Followers(request.form['username'], request.form['password'])
        followers_list = followers.get_followers_list()
    return render_template('/home.html', followers_list = followers_list)

if __name__ == '__main__':
    app.run(debug = True)

