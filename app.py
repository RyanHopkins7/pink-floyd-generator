from flask import Flask
from markov_model import generate_markov_model
from random import choice

app = Flask(__name__)

with open('corpus/pinkfloyd.txt') as f:
    words = f.read().split(' ')

mkv = generate_markov_model(words)

@app.route('/')
def index():
    output = []
    keys = list(mkv.keys())
    current_word = mkv[choice(keys)].sample()

    for _ in range(100):
        current_dict = mkv[current_word]
        current_word = current_dict.sample()
        output.append(current_word)

    return ' '.join(output)

if __name__ == '__main__':
    app.run(debug=True)
