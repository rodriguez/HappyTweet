def merge_dict(d):
    r = {}
    for x in d:
        for k, v in x.items():
            try:
                if r[k]:
                    r[k].append(v)
            except KeyError:
                r[k] = [v]
    return r


def average_dict(d):
    rr = {}
    for k, v in d.items():
        rr[k] = sum(v) / len(v) * 1.0
    return rr
    return max(rr, key=rr.get)
