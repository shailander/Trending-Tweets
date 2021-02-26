# from creds import *
import os
from tweepy import OAuthHandler, API
from dotenv import load_dotenv
load_dotenv()


consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


def authentication():
    print('\nAuthenticating\n')
    # Consumer key authentication(consumer_key,consumer_secret can be collected from our twitter developer profile)
    auth = OAuthHandler(consumer_key, consumer_secret)

    # Access key authentication(access_token,access_token_secret can be collected from our twitter developer profile)
    auth.set_access_token(access_token, access_token_secret)

    # Set up the API with the authentication handler
    api = API(auth)
    print('\nAuthentication completed\n')
    return api

def search_woeid(api, name):
    data = api.trends_available()
    # list = []
    for item in data :
        # list.append({'country' : item['name'], 'woeid' : item['woeid']})
        if item['name'].lower() == name.lower() :
            return item['woeid']
    return 1

def data_fetching(api,woeid):
    print('\nData Fetching\n')
    # woeid = 23424848  # India
    # fetching the trends
    trends = api.trends_place(id=woeid)
    data = []
    n = 1
    for value in trends:
        for trend in value['trends']:
            data.append({'number': n, 'tweet': trend['name'], 'count': trend['tweet_volume']})
            n += 1
    print('\nData Fetching Completed\n')
    return data[:20]

def data_cleaning(data):
    print('\nData Cleaning\n')
    for item in data:
        if item['count'] == None :
            item['count'] = 0
    return data