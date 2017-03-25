import indicoio

indicoio.config.api_key = 'b2ff22240dc7532835daca4712d48bfb'


class EmotionCalc:
    def __init__(self, age, tweet):
        self.tweet = tweet
        self.age = age

    def __repr__(self):
        s = 'Name:' + self.name + '\n'
        s += 'Tweet:' + self.tweet + '\n'

    def mostlikelyemotion(self):
        # single example
        print(indicoio.emotion("I did it. I got into Grad School. Not just any program, but a GREAT program. :-)"))
        test = indicoio.emotion("I did it. I got into Grad School. Not just any program, but a GREAT program. :-)")

        # batch example
        # emolist = indicoio.emotion([
        #    "I did it. I got into Grad School. Not just any program, but a GREAT program. :-)",
        #    "Like seriously my life is bleak, I have been unemployed for almost a year."
        # ])
        print(max(test, key=test.get))
