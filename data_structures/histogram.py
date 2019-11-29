import random
import json
import itertools
import bisect

"""
This is actual data structure used by my Markov chain.
It is custom built from the ground up for optimal effiency and minimal redundency.
"""

class Histogram(dict):
    """ 
    Custom histogram class uses cache of sums and keys for log(n) sampling.
    """

    def __init__(self, d={}, word_list=[]):
        """
        Initialize this histogram dict with data from either an existing histogram or a list of words.
        Args:
            d (dict): A histogram to initialize current object's data off of. Can leave blank.
            word_list (list): A list of words to initialize the histogram's data off of. Can leave blank.
        """

        # List of cached sums of previous values in the hist used for sampling. Parallel to words.
        self.sums = []
        # List of cached keys in the hist used for sampling. Parallel to sums.
        self.words = []

        for word in word_list:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

        super().__init__(d)

        self.update_cache()

    def update_cache(self):
        """
        After modifying items in the histogram, it's necessary to call update_cache.
        Updates the sums and words cache using data from the histogram.
        """
        for i, v in enumerate(self.items()):
            key, value = v
            if i > 0:
                value += self.sums[i-1]

            try:
                self.sums[i] = value
                self.words[i] = key
            except IndexError:
                self.sums.append(value)
                self.words.append(key)

        # If items are removed from dict, remove them from cache
        del self.sums[i+1:]
        del self.words[i+1:]
    
    def sample(self):
        '''
        Randomly samples a key from a histogram with probability based on the value of each key.
        Uses binary search to do this in O(log(n)) time.
        Returns:
            str: word randomly selected in a weighted way from histogram
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
    test_hist = Histogram(word_list=['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    print(test_hist.sample())
    test_hist_sample(test_hist)
