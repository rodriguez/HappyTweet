from flask import Flask, render_template, request
from bson.json_util import dumps
from flask import json
from flask_cors import CORS, cross_origin

from happy_tweet.emotionTest import max_average_emo, region_average_emo
from happy_tweet.emotions import EmotionCalc
from happy_tweet.twitter import User
from happy_tweet.twitter import get_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app)

@app.route('/analyze/average/<username>')
def analyze_average(username):
    try:
        r = max_average_emo(username)
        # return render_template('chart.html', pydata=json.dumps(r))
        return json.dumps(r)
    except:
        return {"error": "Something is wrong"}


@app.route('/analyze/max/<username>')
def analyze_max(username):
    try:
        r = max_average_emo(username)
        r = max(r, key=r.get)
        return json.dumps(r)
    except:
        return {"error": "Something is wrong"}


@app.route('/region/average/<region>')
def region_average(region):
    try:
        r = region_average_emo(region)
        return json.dumps(r)
    except:
        return {"error": "Something is wrong"}

@app.route('/user/<username>')
def user_into(username):
    user = get_user(username)
    return json.dumps(user)


@app.route('/chart')
def get_chart():
    return render_template('chart.html')

if __name__ == "__main__":
    app.run(debug=False)
