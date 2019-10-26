def dict_histogram(words):
    hist = {}
    for word in words:
        if word in hist:
            hist[word] += 1
        else:
            hist[word] = 1
    return hist

def list_histogram(words):
    hist = {}
    for word in words:
        if word in hist:
            hist[word] += 1
        else:
            hist[word] = 1
    return list(map(list, hist.items()))

def tuple_histogram(words):
    hist = {}
    for word in words:
        if word in hist:
            hist[word] += 1
        else:
            hist[word] = 1
    return hist.items()

with open('theparochialhistoryofcornwall.txt') as f:
    words = f.read().split(' ')

