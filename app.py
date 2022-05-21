from flask import Flask, render_template
from spoticolor import current_playing_color

app = Flask(__name__)


@app.route('/')
def hello():
    color = 'background-color: rgb' + str(current_playing_color()) + ';'

    

    # print(color)

    # f = open('templates/main.html', 'w')
    

    # document = '<!DOCTYPE html><html><body style="background-color:' + color + ' ;"></body></html>'
    # f.write(document)
     #f.close()
    return render_template('main.html', clr = color)