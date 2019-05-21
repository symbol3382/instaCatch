from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test2'
# Tried but didn't help
app.config['MYSQL_CHARSET'] = 'utf8mb4'
mysql = MySQL(app)

@app.route('/')
def test2():
    return render_template('test2.html')

@app.route('/insert_emoji_test', methods=['POST'])
def insert_emoji_test():
    myinput = request.form['myinput']
    print('MyInput : \t' , myinput)
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO test2 VALUES (%s)', (myinput,))
    print('INSERT INTO test2 VALUES (%s)', (myinput,))
    mysql.connection.commit()
    cur.close()
    return render_template('test2_result.html', result = myinput)

if __name__ == '__main__':
    app.run(debug = True)