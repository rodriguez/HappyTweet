import indicoio
from happy_tweet.twitter import User


def individual_happiness(tweet_data):
    date_happy = {}
    for x in tweet_data:
        max_emote = indicoio.emotion(x["text"])
        date_happy[x["time"]] = max_emote["joy"]
    return date_happy

def emo_tweet(tweet):
    # return indicoio.emotion(tweet)
    print("Here" + tweet)
    return 0


def individual_happiness(tweets):
    for tweet in tweets:
        text = tweet['text']
        emotion = emo_tweet(text)
        tweet['emotion'] = emotion
    return tweets


if __name__ == '__main__':
    u = User('@gaspardetienne9')
    print(individual_happiness(u.get_tweets()))
