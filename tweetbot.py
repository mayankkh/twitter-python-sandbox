#!flask/bin/python

import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweets = ['Tweet 1!!!', 'Tweet 2!!!', 'Tweet 3!!!']

for tweet in tweets: 
    api.update_status(tweet)
    print (tweet)
    time.sleep(10) 

