import tweepy
from textblob import TextBlob

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

request_tweets = api.search("Trump")

for tweet in request_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
