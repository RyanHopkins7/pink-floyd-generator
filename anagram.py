import sys

def anagram(word):
    '''
    Given a string, return its anagrams if they exist
    Args:
        word: a word to anagram
    Returns:
        List of all anagrams of word from corpus words.txt
    '''
    with open('words.txt', 'r') as corpus:
        real_words = corpus.read().split('\n')
    
    # Generate histograms of letters for each word in real_words
    for i, real_word in enumerate(real_words):
        real_word_hist = {}
        for l in real_word:
            if l in real_word_hist:
                real_word_hist[l] += 1
            else:
                real_word_hist[l] = 0
        real_words[i] = (real_word_hist, real_word)

    # Generate histogram of letters for word
    word_hist = {}
    for l in word:
        if l in word_hist:
            word_hist[l] += 1
        else:
            word_hist[l] = 0

    anagrams = []

    # Compare histograms
    for real_word_hist, real_word in real_words:
        if real_word_hist == word_hist:
            anagrams.append(real_word)

    return anagrams



if __name__ == '__main__':
    word = sys.argv[1]
    print(anagram(word))
