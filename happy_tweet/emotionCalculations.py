import indicoio
from happy_tweet.twitter import User

indicoio.config.api_key = 'b2ff22240dc7532835daca4712d48bfb'


class EmotionCalc:
    def __init__(self, name, age, location, tweet):
        self.name = name
        self.tweet = tweet
        self.age = age
        self.location = location

    def __repr__(self):
        s = 'Name:' + self.name + '\n'
        s += 'Tweet:' + self.tweet + '\n'
        s += 'Location' + self.location + '\n'

    def mostlikelyemotion(self):
        # single example
        # print(indicoio.emotion(self.tweet))
        test = indicoio.emotion(self.tweet)

        return max(test, key=test.get)


def user_data(TwitterHandle):
    # BREAK UP TWITTER DATA HERE probs using the API
    # i.e. EmotionCalc(Paul, 34, Boston, "Pie is good.")
    # If something is null, return "N/A"

    # [Paul, 34, Boston, "Pie is good."]
    # [Cindy, nullorwhatever ,Boston, "Cake is good."]
    # if null, increment the index

    personData = []
    personData += EmotionCalc.name
    personData += EmotionCalc.age
    personData += EmotionCalc.location
    personData += EmotionCalc.tweet
    personData += EmotionCalc.mostlikelyemotion()
    return personData


def total_data(AllTweets):
    allData = []
    for x in AllTweets:
        allData += [user_data(x)]

    return allData


def individual_happiness(tweet_data):
    date_happy = {}
    # [ { ] { } { }]
    # { } { }
    # key, value key, value
    # return dict["time"], indico.emotion(dict["text"])

u = User('@gaspardetienne9')
print(individual_happiness(u.get_tweets()))


