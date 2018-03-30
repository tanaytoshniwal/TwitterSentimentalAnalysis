import tweepy
from textblob import TextBlob

consumer_key = "SHIJizmiH2qu2MjGDY4LGAaJe"
consumer_secret = "aafcmTRmacGsyry6UCkiZ7G5EVODYJA3ce2zRVEp6sNTW8f4xk"

access_token = "2780429452-Dgc0sPtzFoyv2FLv8zgn9WqETRU2eMeIH8BtDpq"
access_token_secret = "vhm7FNd8agksQTTkpG6pXlq8nnzN39jfTtkP4UdohqLKu"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

request_tweets = api.search("Trump")

for tweet in request_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)