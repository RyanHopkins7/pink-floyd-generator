import random
import json
import itertools
import bisect

class Dictogram(dict):
    """ 
    Custom dictogram class uses cache of sums and keys for log(n) sampling.
    """

    def __init__(self, d=None, word_list=None):
        """Initialize this histogram as a new dict and add sum."""

        # List of cached sums of previous values in the hist used for sampling. Parallel to words.
        self.sums = []
        # List of cached keys in the hist used for sampling. Parallel to sums.
        self.words = []

        if d is None:
            d = {}
        if word_list is None:
            word_list = []

        for word in word_list:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

        super().__init__(d)

        self.update_cache()

    def update_cache(self):
        """
        After modifying items in the dictogram, it's necessary to call update_cache.
        Updates the sums and words cache using data from the histogram.
        """
        i = 0
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
