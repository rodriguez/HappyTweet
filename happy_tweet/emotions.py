import indicoio
import sys

indicoio.config.api_key = 'b2ff22240dc7532835daca4712d48bfb'


class EmotionCalc:
    @staticmethod
    def most_likely_emotion(tweet):
        """
        Predict the most likely emotion
        :param tweet: A string of text
        :return: A string that indicate that tweet's sentiment
        """
        test = indicoio.emotion(tweet)
        return max(test, key=test.get)

    @staticmethod
    def get_all_emotions(tweet):
        """
        Wrapper around the indico.io API
        :param tweet: A string of text
        :return: A dict of sentiments of that tweet
        """
        try:
            r = indicoio.emotion(tweet)
        except:
            print("Something wrong happened here: " + sys.exc_info()[0])
