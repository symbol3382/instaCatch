from flask import Flask, render_template, request, url_for, redirect
from Followers import Followers
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'instacatch'
app.config['MYSQL_CHARSET'] = 'utf8mb4'
mysql = MySQL(app)

MAX_ROWS_INSERT = 32500

# to check the user is present or not


def check_user_exist(username):
    cur = mysql.connection.cursor()
    cur.execute('SELECT id from `user` WHERE username=%s', (username,))
    current_user_count = len(cur.fetchall())
    cur.close()
    return current_user_count

# to insert user for new users


def insert_user_if_not_exist(username, followers):
    if True:
        # user is not exist so do
        # 1. Add user to instacatch.user table
        # 2. Add user's follower list to instacatch.user_follower table

        # 1. Add user to user table
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
            sql_query = 'INSERT INTO `user_follower`(`user_id`, `follower_username`, `follower_name`) VALUES '
            followers_insert_list = []

            i = 0

            for x in followers:
                follower_fullname = x.full_name.replace("'", "\\\'")
                follower_fullname = follower_fullname.replace("#", "\#")
                follower_username = x.username.replace("'", "\\\'")
                follower_username = follower_username.replace("#", "\#")
                followers_insert_list.append('('+str(user_id) + ',\'' + follower_username + '\',\'' + follower_fullname + '\')')

            insert_list = ','.join(followers_insert_list)
            sql_query += insert_list
            print(sql_query)
            cur.execute(sql_query)
            mysql.connection.commit()
        cur.close()
    else:
        # So user is not new, now compare list of user followers with previous
        print('user is not new')
    print(sql_query)
    return sql_query

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_login', methods=['POST'])
def check_login():
    if request.method == 'POST':
        followers = Followers(request.form['username'], request.form['password'])
        followers_list = followers.get_followers_list()
        username = request.form['username']
        sql_query = insert_user_if_not_exist(username, followers_list)
    print(sql_query)
    return render_template('test.html', result = sql_query)
    # return render_template('/home.html', followers_list = followers_list)

if __name__ == '__main__':
    app.run(debug = True)

# To add the user to database
def add_user():
    cur = mysql.connection.cursor()
    username = request.form['username']
    cur.execute('INSERT INTO `user` (username) VALUES(%s)', (username))
    mysql.connection.commit()
    cur.close()
