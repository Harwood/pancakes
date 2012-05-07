#!/usr/bin/env python

import base64
import getpass
import json
import urllib
import urllib2
import time
import datetime
import pprint
import pickle
import MySQLdb
#import sqlite3


def fetch(uri, username='', password='', data=None):
  
  headers = {}
  if username and password:
    headers['Authorization'] = 'Basic ' + base64.b64encode('%s:%s' % (username,
        password))
    headers['User-Agent'] = 'TwitterStreamingSample'
  
  req = urllib2.Request(uri, headers=headers)
  if data:
    req.add_data(urllib.urlencode(data))
  f = urllib2.urlopen(req)
  return f




def main():
  #Specify your username and passowrd
  username = 'carterwharwood'
  password = 'v3sf0f98'

  print
  
  try:
 
    ######  Connection established with the database -UNCOMMENT THE BELOW CODE, Incase you want to use a DB
  #  db = MySQLdb.connect(host="localhost", user="", passwd="",
#	db="tweets")
#	cursor = db.cursor()

    track="USA"
     
    f = fetch('https://stream.twitter.com/1/statuses/filter.json', username,
        password, {'track': track})
    #incase you want random sample, use this
    #f = fetch('https://stream.twitter.com/1/statuses/sample.json', username,
    #    password)
    print 'Tracking... [Control + C to stop]'
    print
    multiline = False
    line = ''

    while True:
      if multiline:
        line += '\n' + f.readline()
      else:
        line = f.readline()

      multiline = not line.endswith('\r\n')
      if multiline:
        continue
      
      if line:
        status = json.loads(line)
#        print status
        try:

          
##### Table 1 - Tweets Table #####
          
	  t2_text=status['text']
	  print "Tweet: "+t2_text
	  t_id=status['id']
	  print
	  print "By user: "+str(t_id)
	  print

	  t2_geo = str(status['geo'])
	  t_tweet_truncated = str(status['truncated'])
	  t2_coord = str(status['coordinates'])
          str1=str(status['in_reply_to_user_id'])
	  if str1 == 'None':
                t_tweet_in_reply_to_user_id = 0
          else:
                t_tweet_in_reply_to_user_id = status['in_reply_to_user_id']
	  t_tweet_created_at = str(status['created_at'])
	  t2_ent = str(status['entities'])
	  t_tweet_favorited = str(status['favorited'])
	  t_tweet_in_reply_to_status_id_str = str(status['in_reply_to_status_id_str'])
	  t2_place = str(status['place'])
	  t_tweet_in_reply_to_screen_name = str(status['in_reply_to_screen_name'])
	  t_tweet_in_reply_to_user_id_str = str(status['in_reply_to_user_id_str'])
	  t_tweet_id_str = str(status['id_str'])
	  t2_contri = str(status['contributors'])
	  t_tweet_retweeted = str(status['retweeted'])

          if 'retweeted_status' in status:
		t2_retweeted_status = str(status['retweeted_status'])
          else:
                t_retweeted_status = "NA"          
	  

          t_user_id1     =status['user']['id']
          
########## DATABASE ENTRY ##########

          #sqlstr1 = "WRITE QUERY TO INSERT INTO TWEETS TABLE"
          #cursor.execute(sqlstr1.encode('utf8'))

##### Table 2 - User Table #####
	  t_user_profile_background_tile	=	status['user']['profile_background_tile']
          t_user_contributors_enabled	=	status['user']['contributors_enabled']
          t_user_statuses_count	=	status['user']['statuses_count']
          t_user_followers_count	=	status['user']['followers_count']
          t_user_profile_image_url	=	status['user']['profile_image_url']
          t_user_is_translator	=	status['user']['is_translator']
          t_user_favourites_count	=	status['user']['favourites_count']
          t_user_profile_link_color	=	status['user']['profile_link_color']
          t2_loc	=	status['user']['location']
          t_user_listed_count	=	status['user']['listed_count']
          t_user_profile_sidebar_border_color	=	status['user']['profile_sidebar_border_color']
          t2_desc	=	status['user']['description']
          t2_sname	=	status['user']['screen_name']
	  t_time  =       status['user']['time_zone']
	  t_user_verified	=	status['user']['verified']
          t_user_notifications	=	status['user']['notifications']
          t_user_profile_use_background_image	=	status['user']['profile_use_background_image']
          t_user_created_at	=	status['user']['created_at']
          t_user_friends_count	=	status['user']['friends_count']
          t_user_profile_background_color	=	status['user']['profile_background_color']
          t_user_default_profile_image	=	status['user']['default_profile_image']
          t_user_lang	=	status['user']['lang']
          t_user_profile_background_image_url	=	status['user']['profile_background_image_url']
          t_user_protected	=	status['user']['protected']
          t2_name	=	status['user']['name']
          t_user_id_str	=	status['user']['id_str']
          t_user_default_profile	=	status['user']['default_profile']
          t_user_show_all_inline_media	=	status['user']['show_all_inline_media']
          t_user_geo_enabled	=	status['user']['geo_enabled']
          t_user_profile_text_color	=	status['user']['profile_text_color']
          t_user_id	=	status['user']['id']
          t_user_follow_request_sent	=	status['user']['follow_request_sent']
          t_user_following	=	status['user']['following']
          t_user_utc_offset	=	status['user']['utc_offset']
          t_user_profile_sidebar_fill_color	=	status['user']['profile_sidebar_fill_color']
          t_user_url	=	status['user']['url']


########## DATABASE ENTRY ##########

          #sqlstr1 = "WRITE QUERY TO INSERT INTO USERS TABLE"
          #cursor.execute(sqlstr1.encode('utf8'))




######### ENTITIES TABLES - parsing and database entry #######
          
	  for urls in status['entities']['urls']:
          	t_tweet_id = t_id 
		t_url = str(urls['url'])
		t_expanded_url = str(urls['url'])
		#sqlstr3 = "INSERT INTO tweet_urls (tweet_id, url, expanded_url) VALUES ('%s','%s','%s')" % (t_tweet_id, t_url, t_expanded_url) 
	  	#cursor.execute(sqlstr3.encode('utf8'))


          for user_mentions in status['entities']['user_mentions']:
		t_tweet_id = t_id 
		t_source_user_id = t_user_id
		t_target_user_id = user_mentions['id']
		#sqlstr4 = "INSERT INTO tweet_mentions (tweet_id, source_user_id,target_user_id) VALUES ('%s','%s','%s')" % (t_tweet_id, t_source_user_id,t_target_user_id)      
                #cursor.execute(sqlstr4.encode('utf8'))


          for hashtags in status['entities']['hashtags']:
                t_tweet_id = t_id
                t_hashtags = hashtags['text']
                #sqlstr5 = "INSERT INTO tweet_hashtags (tweet_id, hashtag) VALUES ('%s','%s')" % (t_tweet_id, t_hashtags)
                #cursor.execute(sqlstr5.encode('utf8'))





##### EXCEPTION HANDLING #####
#        except MySQLdb.IntegrityError, e:
#	  pass
#	except MySQLdb.Error, e:
#     	  print "Error %d: %s" % (e.args[0], e.args[1])
#          pass
        except KeyError, e:
          continue

	
	#except:
         # print "\n error in processing tweet: \n"
	  
	
      else:
        time.sleep(0.1)
        
  except urllib2.HTTPError, e:
    # Deal with unexpected disconnection
    #raise e
    time.sleep(10)
    #pass
  except KeyboardInterrupt:
    # End
    f.close()
    print 'Bye!'


if __name__ == '__main__':
  main()




