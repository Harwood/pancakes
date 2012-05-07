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
		self.id, self.name, self.username, self.text = get_tweet_info(i)


	def get_tweet_info(tweet):
		return self.id, self.name, self.username, self.text

def print_results(results):
	for i in results:
		print(i)
		id, name, username, text = get_tweet_info(i)
		print(id		print(name)
		print(username)
		print(text)
		print
