import tweepy
import json

# todo: print(age)
# The consumer keys and access tokens which are used
CONSUMER_KEY = 'nQ09IRj8CzPCG1bxUIva3HSKW'
CONSUMER_SECRET = 'CfAR02mGVYsnOcnb1DDOjgeYGLayyfwVqqFAtA8WBluc5Tpyeo'
ACCESS_TOKEN = '1564136786-INIswUQ1fRFeIv8QhVDtBr6yGeRwP6sUdeUxkfm'
ACCESS_TOKEN_SECRET = '0BU8huIvlY7S94ed5s8muSqmlctf4w8aSv4hh6YRaMp6R'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



class User:
    def __init__(self, username):
        self.username = username
        self.user = api.get_user(username)
        self.user_id = self.user.id

    def get_data(self):
        """
        Get data for an user
        :return: A dict of user data
        """
        return self.user

    def get_tweets(self):
        tweets = api.user_timeline()
        tweets = [self.process_tweet(tweet) for tweet in tweets]
        return tweets

    def process_tweet(self, tweet):
        return {
            "time": tweet.created_at,
            "text": tweet.text,
            "id": tweet.id,
            "user_id": self.user_id
        }


class Search:
    pass


def test():
    # Test with user '@gaspardetienne9'
    u = User('@gaspardetienne9')
    print(u.get_tweets())
    u.get_data()


if __name__ == '__main__':
    test()
