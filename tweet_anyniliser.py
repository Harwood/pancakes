import sys
import argparse
import sqlite3
import tweet_util
import re

def arg_handling():
	parser = argparse.ArgumentParser(description='Tweet analyser')
	try:
		parser.add_argument('-t',nargs=1, dest='tweets_db', type=str, default=[''], required=True, help='sqlite database storing tweets')
		parser.add_argument('-p',nargs=1, dest='pos_neg_table', type=str, default=[''], required=True, help='table that holds positive and negitive words')
		parser.add_argument('-s',nargs=1, dest='sides_table', type=str, default=[''], required=True, help='table that holds words relating to each side')


	except Exception as err:
		print('Argument error: ')
		print(err)
		sys.exit()

	args = parser.parse_args()

	return args.tweets_db[0],  args.pos_neg_table[0], args.sides_table[0]

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


# Checks if word exists
def contains_word(text,word,case_sensitive):
    if re.search(word,text) is not None:
        print ('Found')
        return True
    else:
        print ('Not Found')
        return False


def test_db(db):
	return get_results(db,'select * from tweet')


# Main driver
def main():
	tweets_db, pos_neg_table, sides_table = arg_handling()


	tweet_util.print_results(get_results(tweets_db,'select * from tweet order by user'))
	print(tweets_db)
	print(pos_neg_table)
	print(sides_table)
	#print(db_connect(tweets_db,pos_neg_table,'word'))


if __name__ == "__main__":
	main()
