import indicoio

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


def individual_happiness(list_of_tweets):
    list_of_dicts = []
    for x in list_of_tweets:
        list_of_dicts += indicoio.emotion(x)

    avg_dict = {}
    for list_of_dicts[x] in list_of_dicts:
        # make sad, and such
        if x not in avg_dict:
            avg_dict[x] = list_of_dicts[x]
        else:
            avg_dict[x] += list_of_dicts[x]
