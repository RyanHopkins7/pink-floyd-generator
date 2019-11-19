from data_structures.histogram import Histogram
import json
from random import choice

def generate_markov_model(word_list):
    markov_model = {}

    # Never adds last word in list to markov_model
    for i, word in enumerate(word_list[:-1]):
        if word in markov_model:
            if word_list[i+1] in markov_model[word]:
                markov_model[word][word_list[i+1]] += 1
            else:
                markov_model[word][word_list[i+1]] = 1
        else:
            markov_model[word] = Histogram(word_list=[word_list[i+1]])

    for histo in markov_model:
        markov_model[histo].update_cache()

    return markov_model

if __name__ == '__main__':
    with open('corpus/pinkfloyd.txt') as f:
        words = f.read().split()

    mkv = generate_markov_model(words)

    output = []
    keys = list(mkv.keys())
    current_word = mkv[choice(keys)].sample()

    for _ in range(10):
        current_hist = mkv[current_word]
        current_word = current_hist.sample()
        output.append(current_word)

    print(output)
