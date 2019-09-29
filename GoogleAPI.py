# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import tweepy_module
import json

# Instantiates a client
client = language.LanguageServiceClient()

# Import the json file
with open('./hongkong.json','r') as load_f:
    tweets = json.load(load_f)
    print(tweets[0]['text'])

'''tweets[''] = [8200,{1:[['Python',81],['shirt',300]]}]
#print(load_dict)

with open("../config/record.json","w") as dump_f:
    json.dump(load_dict,dump_f)'''

# The text to analyze
score = {}
magnitude = {}
for i in range(len(tweets)):
    document = types.Document(
    content=tweets[i]['text'],
    type=enums.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text
    try:
        sentiment = client.analyze_sentiment(document=document).document_sentiment
    except BaseException:
        continue

    score[i] = sentiment.score
    magnitude[i] = sentiment.magnitude
    print('\n','\n')
    print('Text: {}'.format(tweets[i]['text']))
    print('Sentiment: {}, {}'.format(score[i], magnitude[i]))

filename = './hongkongsentiment.json'
with open(filename, 'w') as file_obj:
    json.dump(score, file_obj)

print('Avarage Score:',sum(score.values())/len(score))
