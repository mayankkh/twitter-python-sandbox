#!flask/bin/python

import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def getTrends():
    trends1 = api.trends_place(1)
    return trends1

def getTrendNames():
    trends1 = api.trends_place(1)
    data = trends1[0] 

    # grab the trends
    trends = data['trends']

    # grab the name from each trend
    names = [trend['name'] for trend in trends]

    # put all the names together with a ' ' separating them
    trendsName = ' '.join(names)
 
    return trendsName 
