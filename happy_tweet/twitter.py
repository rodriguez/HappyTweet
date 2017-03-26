# Todo: print(age)

import tweepy
from flask import json
from flask.json import dumps

from happy_tweet.db import insert, search, search_many
from happy_tweet.emotions import EmotionCalc

# Twitter secrets
CONSUMER_KEY = 'nQ09IRj8CzPCG1bxUIva3HSKW'
CONSUMER_SECRET = 'CfAR02mGVYsnOcnb1DDOjgeYGLayyfwVqqFAtA8WBluc5Tpyeo'
ACCESS_TOKEN = '1564136786-INIswUQ1fRFeIv8QhVDtBr6yGeRwP6sUdeUxkfm'
ACCESS_TOKEN_SECRET = '0BU8huIvlY7S94ed5s8muSqmlctf4w8aSv4hh6YRaMp6R'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


class User:
    def __init__(self, username, location=None):
        self.username = username
        self.user = api.get_user(username)
        self.user_id = self.user.id
        self.location = location

    def get_data(self):
        """
        Get data for an user
        :return: A dict of user data
        """
        return self.user

    def get_tweets(self):
        tweets = self.user.timeline()
        self.tweets = [self.process_tweet(tweet) for tweet in tweets]
        self.insert_tweet({
            '_id': "u_" + str(self.user_id),
            'tweets': self.tweets,
            'username': self.username[1:],
            'user': self.user._json,
            'location': self.location,
        })
        return tweets

    def process_tweet(self, tweet):
        return {
            "time": tweet.created_at.strftime('%m/%d/%y'),
            "text": tweet.text,
            "_id": tweet.id,
            "user_id": self.user_id,
            "emotions": EmotionCalc.get_all_emotions(tweet.text)
        }

    @staticmethod
    def insert_tweet(value):
        insert(value, 'tweets')
        return

    def to_json(self):
        return dumps({
            'username': self.username,
            'user_id': self.user_id,
            'tweets': self.tweets
        })


class Search:
    pass


def get_user(username, location=None):
    """
    If there is the user in the database, we will return that user, else error
    :param username: Twitter handle
    :return: User object
    """
    result = search({'username': username}, 'tweets')
    if not result:
        user = User("@{}".format(username), location)
        user.get_tweets()
        return json.loads(user.to_json())
    else:
        return result


def get_users(region='Boston, Mass.'):
    """
    Get user by region
    :param region: String to represent a region, e.g. Boston
    :return: List of user dict of that region
    """
    result = search_many({'location': "Boston, Mass."}, 'tweets')
    print("Got {} users".format(len(result)))
    return result

if __name__ == '__main__':
    u = User('@gaspardetienne9')
    print(u.process_tweet(u.get_tweets()[0]))
