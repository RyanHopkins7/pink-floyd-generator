from flask import Flask
from histogram import dict_histogram
from sample_from_hist import Histograph

app = Flask(__name__)

with open('pinkfloyd.txt') as f:
    words = f.read().split(' ')

hist = Histograph(dict_histogram(words))

@app.route('/')
def index():
    output = []
    for _ in range(10):
        output.append(hist.hist_sample())
    return ' '.join(output)

if __name__ == '__main__':
    app.run(debug=True)
