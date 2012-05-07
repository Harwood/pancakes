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



# Checks if word exists
def contains_word(text,word):
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

	tweets = tweet_util.create_tweet_array(tweet_util.get_results(tweets_db,'select * from tweet order by user'))	
#	tweet_util.print_results(tweet_util.get_results(tweets_db,'select * from tweet order by user'))
	
	for t in tweets:
		t.print_tweet()
		if t.contains('RT'):
			print('Has RT')
		if t.contains('#Virgos'):
			print('Has #Virgos')
		print
		

	print(tweets_db)
	print(pos_neg_table)
	print(sides_table)
	#print(db_connect(tweets_db,pos_neg_table,'word'))


if __name__ == "__main__":
	main()
