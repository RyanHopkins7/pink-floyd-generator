from flask import Flask, render_template
from markov_model import MarkovModel

app = Flask(__name__)

with open('corpus/pinkfloyd.txt') as f:
    words = f.read().split()

mkv = MarkovModel(corpus=words, order=2)

@app.route('/')
def index():
    output = list(mkv.sample(100))

    # Clean output to end at the end of a sentence        
    for i, word in enumerate(reversed(output)):
        if word[-1] in '.?!':
            output = output[:len(output)-i]
            break

    return render_template('index.html', gen_text=' '.join(output))

if __name__ == '__main__':
    app.run(debug=True)
