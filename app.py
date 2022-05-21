from flask import Flask, render_template
from spoticolor import current_playing_color
import os

app = Flask(__name__)


@app.route('/')
def hello():
    color = 'background-color: rgb' + str(current_playing_color()) + ';'

    dir = 'img/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    return render_template('main.html', clr = color)