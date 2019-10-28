def dict_histogram(words):
    hist = {}
    for word in words:
        if word.lower() in hist:
            hist[word.lower()] += 1
        else:
            hist[word.lower()] = 1

    # Sort dict by values to see most frequently occuring words
    sorted_word_list = sorted(list( zip(hist.values(), hist.keys()) ))
    sorted_word_list = {keyword: num_occur for num_occur, keyword in sorted_word_list}

    return sorted_word_list

def list_histogram(words):
    return list(map(list, dict_histogram(words).items()))

def tuple_histogram(words):
    return dict_histogram(words).items()

with open('theparochialhistoryofcornwall.txt') as f:
    words = f.read().split(' ')
    print(list_histogram(words))

