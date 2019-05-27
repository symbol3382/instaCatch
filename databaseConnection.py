from flask_mysqldb import MySQL

MAX_ROWS_INSERT = 32500

class DatabaseConnection:

	def __init__(self, app):
		app.config['MYSQL_HOST'] = 'localhost'
		app.config['MYSQL_USER'] = 'root'
		app.config['MYSQL_PASSWORD'] = ''
		app.config['MYSQL_DB'] = 'instacatch'
		app.config['MYSQL_CHARSET'] = 'utf8mb4'
		self.mysql = MySQL(app)
	
	def check_user_db(self, username, password):
		self.username = username

		# check user is alreadey registered or not
		cur = self.mysql.connection.cursor()
		cur.execute('SELECT id from `user` WHERE username=%s', (username,))
		user_fetch = cur.fetchall()

		# user is new then add to database
		if(len(user_fetch) == 0):
			user_type = 'new'
			cur.execute("INSERT INTO `user` (username) VALUES(%s)", (username,))
			self.mysql.connection.commit()
			
			# getting id of new user by searching recently added 
			cur.execute('SELECT id FROM `user` WHERE username=%s', (username,))
			self.user_id = str(cur.fetchall()[0][0])
		else:
			user_type = 'old'
			self.user_id = str(user_fetch[0][0])
		cur.close()
		return self.user_id, user_type

	# to add current user's followers list to database
	def set_user_followers_to_db(self,followers):
		sql_query = 'INSERT INTO `user_follower`(`user_id`, `follower_username`, `follower_name`) VALUES '
		followers_list = []

		for x in followers:
			followers_list.append('('
				+ str(self.user_id) + ',\''
				+ x.username.replace("'", "\\\'").replace("#", "\#") + '\',\'' 
				+ x.full_name.replace("'", "\\\'").replace("#", "\#") + '\')')
			
		sql_query += ','.join(followers_list)

		print('--------------------------------------------------------------------------------------------------------------')
		print('--------------------------------------------------------------------------------------------------------------')
		print(sql_query)
		print('--------------------------------------------------------------------------------------------------------------')
		print('--------------------------------------------------------------------------------------------------------------')
		print('--------------------------------------------------------------------------------------------------------------')

		cur = self.mysql.connection.cursor()
		cur.execute(sql_query)
		self.mysql.connection.commit()
		cur.close()

	def get_followers(self, id):
		sql_query = "SELECT * FROM `user_follower` WHERE `user_id` = " + id

		cur = self.mysql.connection.cursor()
		cur.execute(sql_query)
		self.mysql.connection.commit()
		follower_list = cur.fetchall()
		cur.close()
		return follower_list