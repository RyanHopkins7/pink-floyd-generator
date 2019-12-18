from flask import Flask, render_template
from markov_model import MarkovModel
from random import choice

app = Flask(__name__)

with open('corpus/pinkfloyd.txt') as f:
    words = f.read().split()

mkv = MarkovModel(corpus=words, order=2)

start_states = list(mkv.keys())

@app.route('/')
def index():
    starting_state = choice(start_states)

    output = list(mkv.sample(120, starting_state=starting_state))

    # Clean output to begin at the beginning of a sentence and end at the end of a sentence
    for i, word in enumerate(output):
        if word[0].isupper():
            output = output[i:]
            break

    for i, word in enumerate(reversed(output)):
        if word[-1] in '.?!':
            output = output[:len(output)-i]
            break

    return render_template('index.html', gen_text=' '.join(output))

if __name__ == '__main__':
    app.run(debug=True)
