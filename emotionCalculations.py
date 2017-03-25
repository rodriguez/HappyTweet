import indicoio

indicoio.config.api_key = 'b2ff22240dc7532835daca4712d48bfb'


class EmotionCalc:
    def __init__(self, age, tweet, location):
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

        # batch example
        # emolist = indicoio.emotion([
        #    "I did it. I got into Grad School. Not just any program, but a GREAT program. :-)",
        #    "Like seriously my life is bleak, I have been unemployed for almost a year."
        # ])
        return max(test, key=test.get)
