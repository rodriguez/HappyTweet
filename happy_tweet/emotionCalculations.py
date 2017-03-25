import indicoio
from happy_tweet.twitter import User


def user_data(twitter_handle):
    # BREAK UP TWITTER DATA HERE probs using the API
    # i.e. EmotionCalc(Paul, 34, Boston, "Pie is good.")
    # If something is null, return "N/A"

    # [Paul, 34, Boston, "Pie is good."]
    # [Cindy, nullorwhatever ,Boston, "Cake is good."]
    # if null, increment the index

    person = User(twitter_handle)


    personData = []
    personData += EmotionCalc.name
    personData += EmotionCalc.age
    personData += EmotionCalc.location
    personData += EmotionCalc.tweet
    personData += EmotionCalc.mostlikelyemotion()
    return personData


def emo_tweet(tweet):
    # return indicoio.emotion(tweet)
    print("Here" + tweet)
    return 0

def total_data(AllTweets):
    allData = []
    for x in AllTweets:
        allData += [user_data(x)]

    return allData


def individual_happiness(tweets):
    for tweet in tweets:
        text = tweet['text']
        emotion = emo_tweet(text)
        tweet['emotion'] = emotion
    return tweets


if __name__ == '__main__':
    u = User('@gaspardetienne9')
    print(individual_happiness(u.get_tweets()))
