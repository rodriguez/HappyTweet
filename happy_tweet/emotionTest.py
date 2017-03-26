from flask import json

from happy_tweet.twitter import get_user, get_users
from happy_tweet.emo_calc import merge_dict, average_dict


def max_average_emo(username):
    user = get_user(username)
    tweets = user['tweets']
    emotions = [tweet['emotions'] for tweet in tweets]
    return average_dict(merge_dict(emotions))


def region_average_emo(region):
    users = get_users()
    r = []
    # Analisys for each user
    for user in users:
        try:
            tweets = user['tweets']
            emotions = [tweet['emotions'] for tweet in tweets]
            r.append(average_dict(merge_dict(emotions)))
        except:
            print("Something is wrong here")
            continue
    return average_dict(merge_dict(r))

if __name__ == '__main__':
    username_list = ["JMills21478", "Lynds_eey", "Duuuval", "Norphsidee", "beingmesince96", "april_aries17", "Moliblog",
                     "_stayygorgeous", "JulioCN93", "Hipchec","k1967", "SirAWilliams80", "His_SmokingGun",
                     "elirosstheboss",
                     "ThiahArmani_", "MDCPS", "DannyEspinalHD", "ThiahArmani_", "ijump14", "_Whiitneey", "dominictw",
                     "yesimbby", ]
    r = []
    for username in username_list:
        try:
            emo = max_average_emo(username)
            r.append({
                'username':username,
                'emo':emo,
            })
        except:
            print("Error")
            continue
    print(r)
    tally = [{'fear': 0, 'sadness': 0, 'joy': 0, 'anger': 0, 'surprise': 0 }]
    for x in r:
        if r['emo'] == 'fear':
            tally['fear'] += 1
        elif r['emo'] == 'sadness':
            tally['sadness'] += 1
        elif r['emo'] == 'joy':
            tally['joy'] += 1
        elif r['emo'] == 'anger':
            tally['anger'] += 1
        else:
            tally['surprise'] += 1

    # user = get_user(username_list[0])
    # tweets = user['tweets']
    # emotions = [tweet['emotions'] for tweet in tweets]
    # print(emotions)


