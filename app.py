from flask import Flask, render_template
from markov_model import generate_markov_model
from random import choice

app = Flask(__name__)

with open('corpus/pinkfloyd.txt') as f:
    words = f.read().split()

mkv = generate_markov_model(words)

@app.route('/')
def index():
    output = []
    keys = list(mkv.keys())
    current_word = mkv[choice(keys)].sample()

    for _ in range(100):
        if current_word not in mkv:
            current_word = mkv[choice(keys)].sample()
        current_dict = mkv[current_word]
        current_word = current_dict.sample()
        output.append(current_word)

    # Clean output to start at the beginning of a sentence and end at the end of a sentence
    for i, word in enumerate(output):
        if word[0].isupper():
            output = output[i:]
            break
    i = len(output)
    for word in reversed(output):
        if word[-1] in '.?!':
            output = output[:i]
            break
        i -= 1

    return render_template('index.html', gen_text=' '.join(output))

if __name__ == '__main__':
    app.run(debug=True)
