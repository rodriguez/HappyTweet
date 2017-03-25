from flask import Flask, render_template, request
from bson.json_util import dumps

from happy_tweet.emotions import EmotionCalc
from happy_tweet.twitter import User
from happy_tweet.twitter import get_user

app = Flask(__name__)


@app.route('/analyze')
def analyze_emo():
    user = get_user('')



@app.route('/user/<username>')
def user_into(username):
    user = User("@{}".format(username))
    user.get_tweets()
    return render_template('user.html', user=user.to_json())


@app.route('/chart')
def get_chart():
    return render_template('chart.html')

if __name__ == "__main__":
    app.run(debug=True)
