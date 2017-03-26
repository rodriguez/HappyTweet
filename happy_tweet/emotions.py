import indicoio
import sys

indicoio.config.api_key = '7fcb9bf9ac1dc6d32c3efa1acb7637a8'


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
            return r
        except:
            e = str(sys.exc_info()[0])
            print("Something wrong happened here: " + e)
            return
