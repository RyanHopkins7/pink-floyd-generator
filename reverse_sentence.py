def reverse_sentence(string):
    return ' '.join(string.split(' ')[::-1])

print(reverse_sentence('hi my name is ryan'))