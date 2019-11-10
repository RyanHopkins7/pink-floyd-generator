from data_structures.dictogram import Dictogram

def generate_markov_model(word_list):
    markov_model = {}

    for i, word in enumerate(word_list):
        if word in markov_model:
            markov_model[word]
        else:
            markov_model[word] = Dictogram(word_list=[word])

    for dicto in markov_model:
        dicto.update_cache()

if __name__ == '__main__':
    with open('corpus/pinkfloyd.txt') as f:
        words = f.read().split()
    mkv = generate_markov_model(words)
