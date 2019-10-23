import random
import sys

def select_rand_words(num_words = 1):
    '''
    Selects num_words random words from the words.txt corpus
    Args:
        num_words: number of random words to select
    Returns:
        num_words random words in a String
    '''
    with open('words.txt', 'r') as corpus:
        words = corpus.read().split('\n')

    rand_words = []

    for _ in range(num_words):
        rand_words.append(random.choice(words))

    return(' '.join(rand_words))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(select_rand_words(int(sys.argv[1])))
    else:
        print(select_rand_words())
