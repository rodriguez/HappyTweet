import geocoder
import tweepy
from tweepy.streaming import StreamListener, json
from tweepy import Stream

# The consumer keys and access tokens which are used
from happy_tweet.twitter import get_user

consumer_key = 'nQ09IRj8CzPCG1bxUIva3HSKW'
consumer_secret = 'CfAR02mGVYsnOcnb1DDOjgeYGLayyfwVqqFAtA8WBluc5Tpyeo'
access_token = '1564136786-INIswUQ1fRFeIv8QhVDtBr6yGeRwP6sUdeUxkfm'
access_token_secret = '0BU8huIvlY7S94ed5s8muSqmlctf4w8aSv4hh6YRaMp6R'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.get_user('@marty_walsh')
location = user.location
geocode_location = geocoder.google(location)
list_users = []


class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        username = (json.loads(data)['user']['screen_name'])
        print(data)
        while len(list_users) < 1000:
            list_users.append(username)
            get_user(username, location=location)
            return True
        else:
            return False

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = MyStreamListener()
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(locations=geocode_location.geojson['bbox'])
