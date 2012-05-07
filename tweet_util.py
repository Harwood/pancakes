import sys, sqlite3

class Database:
	def __init__(self,db,table, column):
		self.conn , self.curr = self.__connect_db(db)
		self.list = self.__select_db(self.curr,table,column)
		self.__disconnect_db(self.conn,self.curr)

	def get_list():
		return self.list

	# Creates connection and cursor for sqlite db
	def __connect_db(self,db):
		try:
			conn = sqlite3.connect(db)
			curr = conn.cursor()

		except Exception as err:
			print(str(err))
			sys.exit()

		return conn, curr

	# Close connection and cursur for sqlite db
	def __disconnect_db(self,conn,curr):
		try:
			curr.close()
			conn.close()
		except Exception as err:
			print(str(err))
	# Returns tables
	def __select_db(self,curr,table,col):
		try:
			tmp = curr.execute('.tables')

			rows=[]
			for t in tmp:
				rows.append(t[0])
		except Exception as err:
			print(str(err))
			sys.exit()

		return rows
	# Returns list of results from select query
	def __select_db(self,curr,table,col):
		try:
			tmp = curr.execute('select * from '+table+' order by '+col)

			rows=[]
			for t in tmp:
				rows.append(t[0])
		except Exception as err:
			print(str(err))
			sys.exit()

		return rows

class Tweet:
	def __init__(self,tweet):
		self.id = tweet[0]
		self.name = tweet[1]
		self.username = tweet[2]
		self.text = tweet[3]
		self.tweet = tweet

	def get_original_tweet_info(self):
		return self.tweet

	def get_info(self):
		return self.id, self.name, self.username, self.text
	def print_tweet(self):
		print(self.id)
		print(self.name)
		print(self.username)
		print(self.text)
		print


def create_tweet_array(tmp):
	array = []
	for t in tmp:
		array.append(Tweet(t))
	return array

def print_results(results):
	for i in results:
		print(i)
		
		tweet = Tweet(i)
		id, name, username, text = tweet.get_info()
		print(id)
		print(name)
		print(username)
		print(text)
		print

# Connects to databases
def db_connect(db,table,column):
	data = tweet_util.Database(db,table,column)

	return data.get_list()

def get_results(db,query):
	conn = sqlite3.connect(db)
	curr = conn.cursor()

	result = curr.execute(query)
	try:
		rows=[]
		for t in result:
			rows.append(t)
	except Exception as err:
		print("Error printing results: ")
		print(str(err))
		sys.exit()

	curr.close()
	conn.close()


	return rows

