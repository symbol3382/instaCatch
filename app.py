from flask import Flask, render_template, request, url_for, redirect, session

from Followers import Followers
from databaseConnection import DatabaseConnection

app = Flask(__name__)
app.secret_key = 'abc'
db_obj = DatabaseConnection(app)
follower_obj = Followers()

def clear_session():
    session['logged'] = False
    session['username'] = None 
    session['user_id'] = None
    session['new_follower'] = None 
    session['unfollowers'] = None
    session['full_name'] = None
    session['pic_url'] = None
    session['funame'] = None

def get_analysis(user_login_type):
    followers_list = set([])
    followers = follower_obj.get_followers_list()

    new = ''
    unf = ''

    for f in followers:
        followers_list.add((f.username, f.full_name))

    # Compare if user is not new
    if user_login_type == 'old':
        compare_list = set([])
        for row in db_obj.get_followers(session['userid']):
            compare_list.add((row[1], row[2]))
        new = list(followers_list.difference(compare_list))
        unf = list(compare_list.difference(followers_list))

    session['funame'] = list(followers_list)
    session['f_new'] = new
    session['f_un'] = unf

    print('-----------------------------------------------')
    print(new)
    print('-----------------------------------------------')
    print(unf)
    print('-----------------------------------------------')
    print('-----------------------------------------------')

    return new, unf

@app.route('/')
def index():
    msg = request.args.get('message')
    show_message = False if msg == None else True
    return render_template('index.html', error_message=request.args.get('message'), show_message=show_message)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        login_check = follower_obj.login(username, password)

        if(login_check == True):
            clear_session()
            session['logged'] = True
            session['username'] = username
            session['userid'],user_login_type = db_obj.check_user_db(username, password)
            if user_login_type == 'old':
                # analysis of data if user is re logining
                session['new_user'] = False
                n,u = get_analysis(user_login_type)
                session['new_followers'] = n
                session['unfollowers'] = u
            else:
                session['new_user'] = True
                get_analysis(user_login_type)
                db_obj.set_user_followers_to_db(follower_obj.get_followers_list())
            user = follower_obj.get_user(session['username']) # Get user name and dp url
            session['full_name'] = user['full_name']
            session['pic_url'] = user['pic_url']
            return redirect(url_for('home'))
        else:
            return redirect(url_for('index', message=login_check))

@app.route('/home')
def home():
    new_followers = ''
    unfollowers = ''
    if session['new_user'] == False:
        for x in session['unfollowers']:
            print(x)
        new_followers = str(len(session['new_followers']))
        unfollowers = str(len(session['unfollowers']))
    
    return render_template('home.html', new_followers = new_followers, unfollowers = unfollowers)

@app.route('/followers')
def followers():
    return render_template('followers.html')

@app.route('/logout')
def logout():
    clear_session()
    return redirect(url_for('index', message = 'Logged out successfully'))

@app.route('/new-followers')
def new_followers():
    return render_template('new_followers.html')

@app.route('/unfollowers')
def unfollowers():
    return render_template('unfollowers.html')
    
if __name__ == '__main__':
    app.run(debug=True)
