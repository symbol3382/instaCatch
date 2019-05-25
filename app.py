from flask import Flask, render_template, request, url_for, redirect
from Followers import Followers
from databaseConnection import DatabaseConnection

app = Flask(__name__)
db_obj = DatabaseConnection(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		db_obj.check_user_db(username, password)

	return redirect(url_for('home'))

@app.route('/home')
def home():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug = True)
