import sys
import random
import json

def shuffle(arr):
    '''
    Uses the Fisher-Yates shuffle to shuffle a list.
    Args:
        arr: list of elements to shuffle
    '''
    for i in range(len(arr)):
        rand_index = random.randint(0, i)
        arr[rand_index], arr[i] = arr[i], arr[rand_index]

def test_shuffle(arr):
    ''' 
    Tests shuffle to ensure randomness. Prints number off occurances 
    of each value in arr in each index after running shuffle 10000 times.
    If shuffle is acting correctly, each num occurances should be approximately equal.
    '''
    occurances = {}
    for val in arr:
        occurances[val] = [0] * len(arr)

    for _ in range(10000):
        shuffle(arr)
        for i, val in enumerate(arr):
            occurances[val][i] += 1

    print(json.dumps(occurances, indent=4))

if __name__ == '__main__':
    # test_data = sys.argv[1:]
    # test_shuffle(test_data)
    args = sys.argv[1:]
    shuffle(args)
    print(' '.join(args))
