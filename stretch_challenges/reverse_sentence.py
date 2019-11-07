import sys

def reverse_sentence(string):
    return ' '.join(string.split(' ')[::-1])

if __name__ == '__main__':
    print(reverse_sentence(' '.join(sys.argv[1:])))