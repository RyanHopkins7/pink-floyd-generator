import json

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

def list_counts(words):
    word_counts = {}
    for word, count in dict_histogram(words).items():
        if count in word_counts:
            word_counts[count].append(word)
        else:
            word_counts[count] = [word]

    return word_counts

def list_histogram(words):
    word_set = set(words)
    return [[word, words.count(word)] for word in word_set]

    # More effiecient
    # return list(map(list, dict_histogram(words).items()))

def tuple_histogram(words):
    word_set = set(words)
    return list(zip(word_set, map(words.count, word_set)))

    # More effiecient
    # return dict_histogram(words).items()

if __name__ == '__main__':
    with open('theparochialhistoryofcornwall.txt') as f:
        words = f.read().split(' ')
        # File is too large  for tuple hist and list hist
        print(json.dumps(list_counts(words), indent=4))
        # print(json.dumps(list_counts(['hi','i', 'i','a']), indent=4))

