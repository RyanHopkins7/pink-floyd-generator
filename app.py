from flask import Flask
from main_code.histogram import dict_histogram
from dictogram import Dictogram

app = Flask(__name__)

with open('corpus/pinkfloyd.txt') as f:
    words = f.read().split(' ')

hist = Dictogram(dict_histogram(words))

@app.route('/')
def index():
    output = []
    for _ in range(10):
        output.append(hist.sample())
    return ' '.join(output)

if __name__ == '__main__':
    app.run(debug=True)
