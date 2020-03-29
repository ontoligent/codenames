import os
import sys
from flask import Flask, render_template
from lib.codenames import KeyCard


sys.path.insert(0, os.path.dirname(__file__))

app = Flask(__name__)

data = {}

@app.route('/')
def index():
    return render_template('home.html')
    
@app.route('/keycard')
def keycard():
    kc = KeyCard()
    kc.draw_card()
    data['grid'] = kc.grid
    data['team'] = kc.team
    data['gridcode'] = kc.gridcode
    return render_template('keycard.html', **data)
    
@app.route('/keycard/<gridcode>')
def clone_keycard(gridcode):
    kc = KeyCard()
    kc.clone_card(gridcode)
    data['grid'] = kc.grid
    data['team'] = kc.team
    data['gridcode'] = kc.gridcode
    return render_template('keycard.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
