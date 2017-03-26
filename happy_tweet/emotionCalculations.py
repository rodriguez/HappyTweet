import indicoio


def individual_happiness(tweet_data):
    date_happy = {}
    for x in tweet_data:
        max_emote = indicoio.emotion(x["text"])
        date_happy[x["time"]] = max_emote["joy"]
    return date_happy

def average_dict(d):
    r = {}
    for x in d:
        for k, v in x.items():
            try:
                if r[k]:
                    r[k].append(v)
            except KeyError:
                r[k] = [v]
    rr = {}
    for k, v in r.items():
        rr[k] = sum(v)/len(v)*1.0
    return max(rr, key=rr.get)


def greatest_of_avg(d):
    rr = average_dict(d)
    return max(rr, key=rr.get)


if __name__ == '__main__':
    print(average_dict(
        [{"a": 2, "b": 3},
        {"a": 5, "b": 3},
        {"a": 7, "b": 3},
    ]))

