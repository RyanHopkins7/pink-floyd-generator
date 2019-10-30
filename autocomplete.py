import sys

def autocomplete(fragment):
    with open('words.txt', 'r') as corpus:
        words = corpus.read().split('\n')

    possible_words = []

    for word in words:
        if fragment == word[:len(fragment)]:
            possible_words.append(word)

    return possible_words


if __name__ == '__main__':
    print(autocomplete(sys.argv[1]))
