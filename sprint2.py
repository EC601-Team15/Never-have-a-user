from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import json
import credentials
import tweetkeys

# this class is used for authentication.
class Authenticator:

  def get_authentication(self):
    auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    return auth

# search by specific words
class Tweets_Searched_by_Querys:
  def __init__(self):
    self.auth = Authenticator().get_authentication()
    self.user = API(self.auth)   

  def search_tweets(self, query, time, filepath, tweets_number):
    tweets = []
    with open(filepath, 'w') as file:
      for tweet in Cursor(self.user.search, q=query, since=time).items(tweets_number):
        tmp_tweet = tweet._json        
        tweets.append(tmp_tweet)
      tweet_json = json.dump(tweets,file,sort_keys = True,indent = 4)
      file.close()

  def search_tweets_sorted(self, query, time, filepath, tweets_number, subkey):
    tweets = []
    with open(filepath, 'w') as file:
      for tweet in Cursor(self.user.search, q=query, since=time).items(tweets_number):
        tmp_tweet = tweet._json
        tmp_tweet_new = dict([(key, tmp_tweet[key]) for key in subkey])
        tweets.append(tmp_tweet_new)
      tweet_json = json.dump(tweets,file,sort_keys = True,indent = 4)
      file.close()

  def view_keys(self):
    print(tweetkeys.key_list)

'''
['created_at', 'id', 'id_str', 'text', 'truncated', 'entities', 'metadata', 'source', 
 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 
 'in_reply_to_screen_name', 'user', 'geo', 'coordinates', 'place', 'contributors', 'is_quote_status', 
 'retweet_count', 'favorite_count', 'favorited', 'retweeted', 'possibly_sensitive', 'lang']
'''

if __name__ == '__main__':

  example = Tweets_Searched_by_Querys();
  filepath = './test.json'
  querys = ["#unitedAIRLINES"]
  time = "2019-09-20"
  subkeys = ['created_at', 'id', 'text','retweeted' ]
  example.search_tweets_sorted(querys, time, filepath, 10, subkeys)
  
  json_py = json.load(open(filepath, 'r'))
  print(json_py)


