from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
import instaloader

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)


def getFollowers():
    username = 'aadeezgauravatif'
    password = 'test@121'
    obj = instaloader.Instaloader()
    obj.login(username, password)
    profile = instaloader.Profile.from_username(obj.context, username)
    followers = set(profile.get_followers())
    print('@' + username + ' has: ' + str(len(followers)) + ' followers\n')
    result_list = []
    i = 0
    for f in followers:
        follower_username = f.username.replace("'", "\\\'")
        follower_fullname = f.full_name.replace("'", "\\\'")
        follower_fullname = follower_fullname.replace("#", "\#")
        follower_username = follower_username.replace("#", "\#")
        if i == 5:
            break
        i += 1
        result_list.append('(\'' + username + '\',\'' + follower_fullname + '\')')
    result = ','.join(result_list)
    print(result)
    return result


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    query = 'INSERT INTO user (username, fullname) VALUES ' + getFollowers()
    #render_template('test.html', query = query)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return render_template('test.html', query=query)


if __name__ == '__main__':
    app.run(debug=True)


