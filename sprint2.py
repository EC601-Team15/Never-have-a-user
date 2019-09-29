from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import json
import credentials
import tweetkeys
import re

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
class Analysis_1:

  def __init__(self):
    self.client = language.LanguageServiceClient()

  def tweets_analysis(self, filepath, filepath_res):
    with open(filepath, r) as load_f:
      tweets = json.load(load_f)
      print(tweets[0]['full_text'])
    # The text to analyze
      score = {}
      magnitude = {}
      for i in range(len(tweets)):
        document = types.Document(
        content=tweets[i]['text'],
        type=enums.Document.Type.PLAIN_TEXT)
        # Detects the sentiment of the text
        try:
          sentiment = self.client.analyze_sentiment(document=document).document_sentiment
        except BaseException:
          continue

        score[i] = sentiment.score
        magnitude[i] = sentiment.magnitude
        print('\n','\n')
        print('Text: {}'.format(tweets[i]['text']))
        print('Sentiment: {}, {}'.format(score[i], magnitude[i]))
      
      with open(filepath_res, 'w') as file_obj:
          json.dump(score, file_obj)
    print('Avarage Score:',sum(score.values())/len(score))

class Analysis:
  # Instantiates a client
  def __init__(self):
    self.object = TweetsSearch()
    self.client = language.LanguageServiceClient()
# text analyze
  def tweets_analysis(self, query, time, tweets_number, subkey):
    texts = self.object.search_tweets_sorted(query, time, tweets_number, subkey)
    for text in texts:
      document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
      # Detects the sentiment of the text
      sentiment = self.client.analyze_sentiment(document=document).document_sentiment
      print('Text: {}'.format(text))
      print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

# this class is used for authentication.
class Authenticator:

  def get_authentication(self):
    auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    return auth

# search by specific words
class TweetsSearch:

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
      for tweet in Cursor(self.user.search, q=query, tweet_mode = 'extended', since=time).items(tweets_number):
        tmp_tweet = tweet._json      
      tmp_tweet_new = tmp_tweet[subkey]
        # tmp_tweet_new = dict([(key, tmp_tweet[key]) for key in subkey])
        tweet_clean = re.sub(r"http\S+", "", tmp_tweet_new)
        tweets.append(tweet_clean)
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

  example = TweetsSearch()
  sen_analysis = Analysis_1()

  filepath = './test.json'
  filepath_res = './test_res.json'
  querys = ["#unitedAIRLINES"]
  time = "2019-09-20"
  # subkeys = ['created_at', 'id', 'full_text','retweeted']
  subkeys ='full_text' 

  example.search_tweets_sorted(querys, time, 5, subkeys)
  sen_analysis.tweets_analysis(filepath, filepath_res)


