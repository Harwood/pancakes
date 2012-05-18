import sys
import argparse
import sqlite3
import tweet_util
import re

def arg_handling():
	parser = argparse.ArgumentParser(description='Tweet analyser')
	try:
		parser.add_argument('-t',nargs=1, dest='tweets_db', type=str, default=[''], required=True, help='sqlite database storing tweets')
		parser.add_argument('-i', action='count', dest='format for WEKA analysis')


	except Exception as err:
		print('Argument error: ')
		print(err)
		sys.exit()

	args = parser.parse_args()

	return args.tweets_db[0], args.info



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



def get_array_of_tweets(db,query):
	return tweet_util.create_tweet_array(tweet_util.get_results(db,query)) 

def get_array_of_words(db,query):
	return tweet_util.create_word_array(tweet_util.get_results(db,query)) 

def calc_score(tweet,words):
	rep = re.compile('u')
	dem = re.compile('m')
	pos = re.compile('s')
	neg = re.compile('g')

	for w in words:
		if tweet.contains(w.text):
			if w.side is not '':
				if rep.search(w.side.encode('unicode_escape'),re.I):
					#print('Republican: '+str(w.text))
					tweet.inc_rep_score(w.value)
				if dem.search(w.side.encode('unicode_escape'),re.I):
					#print('Democrat: '+str(w.text))
					tweet.inc_dem_score(w.value)
				if pos.search(w.side.encode('unicode_escape'),re.I):
					#print('Positive: '+str(w.text))
					tweet.inc_pos_score(1)
				if neg.search(w.side.encode('unicode_escape'),re.I):
					#print('Negitive: '+str(w.text))
					tweet.inc_neg_score(1)
			#Negation list
			else:
				#print('Negations: '+str(w.text))
				tweet.inc_necgation_score(1)
	tweet.score_tweet()




# Main driver
def main():
	dem_count = 0
	rep_count = 0
	other_count = 0

	tweets_db, info = arg_handling()

	tweets = get_array_of_tweets(tweets_db,'select * from tweet order by user')
	pos_neg_words = get_array_of_words(tweets_db,'select * from pos_neg_words order by word')
	dem_rep_words = get_array_of_words(tweets_db,'select * from dem_rep_words order by word')
	negation_words = get_array_of_words(tweets_db,'select * from negation_words order by word')
	
	
	for t in tweets:
		calc_score(t,dem_rep_words)
		calc_score(t,pos_neg_words)
		calc_score(t,negation_words)
		if info is not None:
			t.print_tweet_info()
		else:
			t.print_tweet()
		
			if t.final_score > 0:
				dem_count += 1
			elif t.final_score < 0:
				rep_count += 1
			else:
				other_count += 1

	if info is None:
		print
		print
		print('Democrat Count: '+str(dem_count))
		print('Republican Count: '+str(rep_count))
		print('Not Identfied Count: '+str(other_count))


		

	
		
	
if __name__ == "__main__":
	main()
