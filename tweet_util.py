import sys, sqlite3, re

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
		
		self.dem_score = 0
		self.rep_score = 0
		self.pos_score = 0
		self.neg_score = 0
		self.negation_score = 0

	def get_original_tweet_info(self):
		return self.tweet

	def get_info(self):
		return self.id, self.name, self.username, self.text
	
	def print_tweet(self):
		#print(self.id)
		#print(self.name)
		#print(self.username)
		print(self.text)
		print('Democrate Score: '+str(self.dem_score))
		print('Republican Score: '+str(self.rep_score))
		print('Positive Score: '+str(self.pos_score))
		print('Negitive Score: '+str(self.neg_score))
		print('Negation Score: '+str(self.negation_score))
		print

	def contains(self,word):
		term = re.compile("(^|[\\W\\b])#?"+word+"s?(:|!|$|[\\W\\b])",re.IGNORECASE);
		if term.search(self.text) is not None:
		#if re.search(,self.text,re.I) is not None:
			#print ('Found')
			return True
		else:
			#print ('Not Found')
			return False

	def inc_dem_score(self,value):
		self.dem_score += value
		return self.dem_score
	def inc_rep_score(self,value):
		self.rep_score += value
		return self.rep_score
	def inc_pos_score(self,value):
		self.pos_score += value
		return self.pos_score
	def inc_neg_score(self,value):
		self.neg_score += value
		return self.neg_score
	def inc_necgation_score(self,value):
		self.negation_score += value
		return self.negation_score


class Word:
	
	def __init__(self,word):
		self.word = word

		length = len(self.word)
		if length is 3:
			self.text = self.word[0]
			self.side = self.word[1]
			self.value = self.word[2]
		if length is 2:
			self.text = self.word[0]
			self.side = self.word[1]
			self.value = ''
		if length is 1:
			self.text = self.word[0]
			self.side = ''
			self.value = ''

	def text(self):
		return self.text
	def side(self):
		return self.side
	def value(self):
		return self.value
	def print_word(self):
		print(self.text+'|'+self.side+'|'+str(self.value))


def create_word_array(tmp):
	array = []
	for t in tmp:
		array.append(Word(t))
	return array

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
		print
		#print(id)
		#print(name)
		print(username)
		print(text)
		print

# Connects to databases
def db_connect(db,table,column):
	data = tweet_util.Database(db,table,column)

	return data.get_list()

def db_insert(db,table, tweets):
	try:
		conn = sqlite3.connect(db)
		curr = conn.cursor()
	
		i = 0
		for t in tweets:
			#print(t)
			try:
				query = 'insert into '+unicode(table)+' values("'+unicode(str(i))+'","'+unicode(str(t[0]))+'","'+unicode(str(t[0]))+'","'+str(t[1])+'","'+unicode(str(t[2]))+'","")'
				#query = "insert into "+unicode(table)+" values('"+unicode(str(i))+"','"+unicode(str(t[0]))+"','"+unicode(str(t[0]))+"','"+unicode(str(t[1]))+"','"+unicode(str(t[2]))+"','')"
				curr.execute(query)
				conn.commit()
			except Exception as err:
				print("did not add tweet number "+str(i))
			i += 1

		curr.close()
		conn.close()

	except Exception as err:
		print("Error inserting: ")
		print(str(err))
		sys.exit()


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

