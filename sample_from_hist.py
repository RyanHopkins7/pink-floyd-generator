import random
import json
import itertools

def hist_sample(hist):
    '''
    Randomly samples a key from a histogram with probability based on the value of each key
    Args:
        histogram
    Returns:
        Key
    '''
    values = hist.values()
    rand = random.randint(0, sum(values))

    s = 0
    for i, val in enumerate(values):
        s += val
        if rand <= s:
            return next(itertools.islice(hist.keys(), i, None))

# print(hist_sample({'red':1, 'fish':4, 'blue':1, 'one':1, 'two':1}))

def test_hist_sample(hist):
    ''' 
    '''
    occurances = {}
    for key in hist:
        occurances[key] = 0

    for _ in range(10000):
        occurances[hist_sample(hist)] += 1

    for key in occurances:
        occurances[key] /= 10000

    print(json.dumps(occurances, indent=4))

test_hist_sample({'red':2, 'fish':1, 'blue':5, 'one':1, 'two':1})
