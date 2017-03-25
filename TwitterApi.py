
import tweepy

# The consumer keys and access tokens which are used
consumer_key = 'nQ09IRj8CzPCG1bxUIva3HSKW'
consumer_secret = 'CfAR02mGVYsnOcnb1DDOjgeYGLayyfwVqqFAtA8WBluc5Tpyeo'
access_token = '1564136786-INIswUQ1fRFeIv8QhVDtBr6yGeRwP6sUdeUxkfm'
access_token_secret = '0BU8huIvlY7S94ed5s8muSqmlctf4w8aSv4hh6YRaMp6R'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.get_user('@gaspardetienne9')
#print(user)
name = user.screen_name
name1 = user.name
location = user.location

print(name)
print(name1)
#todo: print(age)
print(location)
user_tweets = api.user_timeline()
print(user_tweets)


