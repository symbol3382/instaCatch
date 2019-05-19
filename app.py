from flask import Flask, render_template, request, url_for, redirect
from Followers import Followers
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'instacatch'
mysql = MySQL(app)

MAX_ROWS_INSERT = 32500

# to check the user is present or not
def check_user_exist(username):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id from `user` WHERE username=%s", (username,))
    cur.close()
    return len(cur.fetchall())

# to insert user for new users
def insert_user_if_not_exist(username, followers):
    if check_user_exist(username) == 0: 
        # user is not exist so do
        # 1. Add user to instacatch.user table
        # 2. Add user's follower list to instacatch.user_follower table
        
        #1. Add user to user table
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `user` (username) VALUES(%s)", (username,))
        mysql.connection.commit()

        # 2. Add user's followers list to instacatch.user_follower table
        cur.execute('SELECT id FROM `user` WHERE username=%s', (username,))
        user_id = cur.fetchall()[0][0]
        followers_count = len(followers)

        if followers_count > MAX_ROWS_INSERT:
            # handle for exceeding list 
            print('32767 greate followers')
        else:
            sql_query = 'INSERT INTO `user_follower`(`user_id`, `follower_username`, `full_name`) VALUES '
            followers_insert_list = []
            for x in followers:
                followers_insert_list.append('('+str(user_id) + ',' + x.username + ',' + x.full_name + ')')
            insert_list = ','.join(followers_insert_list)
            sql_query += insert_list
            print(sql_query)
        cur.close()
    else:
        # So user is not new, now compare list of user followers with previous
        print('user is not new')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_login', methods=['POST'])
def check_login():
    if request.method == 'POST':
        followers = Followers(request.form['username'], request.form['password'])
        followers_list = followers.get_followers_list()
        username = request.form['username']
        insert_user_if_not_exist(username, followers_list)
    return render_template('/home.html', followers_list = followers_list)

if __name__ == '__main__':
    app.run(debug = True)

# To add the user to database
def add_user():
    cur = mysql.connection.cursor()
    username = request.form['username']
    cur.execute('INSERT INTO `user` (username) VALUES(%s)', (username))
    mysql.connection.commit()
    cur.close()
