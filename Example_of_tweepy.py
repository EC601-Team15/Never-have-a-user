import tweepy
# 填写twitter提供的开发Key和secret
consumer_key = 'CyfnOcBuLxFJC5jVxrQDR2ebz'
consumer_secret = 'VTxIem0goTb81Fo4NGtn9ulkj5mZDGbNATpIkGVkupxJ89YWj6'
access_token = '1172305460256362497-6RBkL1bTZFczKWvGDLVdLhQ916I8WF'
access_token_secret = 'UhfH2ltoyiAHgjFNDYlNMtw1IyVn1ctATU7kCzUBXhcwu'

# 提交你的Key和secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# 获取类似于内容句柄的东西
api = tweepy.API(auth)

print(api)
# 打印其他用户主页上的时间轴里的内容
public_tweets = api.user_timeline('juventusfcen')

for tweet in public_tweets:
    print(tweet.text)
