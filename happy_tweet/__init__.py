from flask import Flask, render_template, request
from happy_tweet.emotionCalculations import EmotionCalc

app = Flask(__name__)


@app.route('/analyze')
def analyze_emo():
    name = request.args.get('name') or "Paul"
    age = request.args.get('age') or "50"
    location = request.args.get('location') or "New York, NY"
    tweet = request.args.get('tweet') or "I hate the guy on the train"
    person = EmotionCalc(name, age, location, tweet)
    return person.mostlikelyemotion()


if __name__ == "__main__":
    app.run(debug=True)
