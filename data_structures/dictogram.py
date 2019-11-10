import random
import json
import itertools
import bisect

class Dictogram(dict):
    """ 
    Custom dictogram class uses cache of sums and keys for log(n) sampling.
    """
    # List of cached sums of previous values in the hist used for sampling. Parallel to words.
    sums = []
    # List of cached keys used for sampling. Parallel to sums.
    words = []

    def __init__(self, d={}, word_list=[]):
        """Initialize this histogram as a new dict and add sum."""

        for word in word_list:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        
        items = list(d.items())
        for i, v in enumerate(items):
            key, value = v
            if i > 0:
                value += self.sums[i-1]
            self.sums.append(value)
            self.words.append(key)

        super().__init__(d)

    def __setitem__(self, key, item):
        if len(self) > 0:
            self.sums.append((self.sums[-1][0] + item, key))
        else:
            self.sums.append((item, key))

        super().__setitem__(key, item)
    
    def sample(self):
        '''
        Randomly samples a key from a histogram with probability based on the value of each key.
        Uses binary search to do this in O(log(n)) time.
        Returns:
            str: word randomly selected in a weighted way
        '''
        if len(self) == 0:
            return None

        rand = random.randint(1, self.sums[-1])
        return self.words[bisect.bisect_left(self.sums, rand)]

def test_hist_sample(hist):
    occurances = {}
    for key in hist:
        occurances[key] = 0

    for _ in range(100000):
        occurances[hist.sample()] += 1

    for key in occurances:
        occurances[key] /= 100000

    print(json.dumps(occurances, indent=4))


if __name__ == '__main__':
    # test_hist = Dictogram({'red':1, 'fish':4, 'blue':1, 'one':1, 'two':1})
    test_hist = Dictogram(word_list=['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    print(test_hist.sample())
    test_hist_sample(test_hist)
