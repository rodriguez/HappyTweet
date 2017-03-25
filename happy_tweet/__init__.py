from flask import Flask, render_template, request
from bson.json_util import dumps

from happy_tweet.emotions import EmotionCalc
from happy_tweet.twitter import User

app = Flask(__name__)


# @app.route('/analyze')
# def analyze_emo():
#     name = request.args.get('name') or "Paul"
#     age = request.args.get('age') or "50"
#     location = request.args.get('location') or "New York, NY"
#     tweet = request.args.get('tweet') or "I hate the guy on the train"
#     person = EmotionCalc(name, age, location, tweet)
#     return person.mostlikelyemotion()

@app.route('/user/<username>')
def user_into(username):
    user = User("@{}".format(username))
    user.get_tweets()
    return render_template('user.html', user=user.to_json())


if __name__ == "__main__":
    app.run(debug=True)
