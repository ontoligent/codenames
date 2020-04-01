import os
import sys
import hashlib
from flask import Flask, render_template, redirect
from lib.codenames import KeyCard, NameCards


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
    data['gridcode'] = kc.gridcode
    return redirect('/keycard/{}'.format(kc.gridcode))
    
@app.route('/keycard/<gridcode>')
def clone_keycard(gridcode):
    kc = KeyCard()
    kc.clone_card(gridcode)
    data['grid'] = kc.grid
    data['team'] = kc.team
    data['gridcode'] = gridcode
    data['hash'] = get_hash(kc.gridcode, 5)
    return render_template('keycard.html', **data)

@app.route('/namecards')
def namecards():
    ncs = NameCards()
    ncs.draw_cards()
    return redirect('/namecards/{}'.format(ncs.cardlist))

@app.route('/namecards/<cardlist>')
def clone_namecards(cardlist):
    ncs = NameCards()
    ncs.clone_cards(cardlist)
    data['grid'] = ncs.grid
    data['cardlist'] = ncs.cardlist
    data['hash'] = get_hash(ncs.cardlist, 5)
    return render_template('namecards.html', **data)

@app.route('/spymaster/<cardlist>')
def get_key_for_game(cardlist):
    kc = KeyCard()
    kc.draw_card()
    return redirect('/spymaster/{}/{}'.format(cardlist, kc.gridcode))

@app.route('/spymaster/<cardlist>/<gridcode>')
def apply_key_to_game(cardlist, gridcode):
    ncs = NameCards()
    ncs.clone_cards(cardlist)
    data['cardgrid'] = ncs.grid
    data['cardlist'] = cardlist
    kc = KeyCard()
    kc.clone_card(gridcode)
    data['keygrid'] = kc.grid
    data['team'] = kc.team
    data['gridcode'] = gridcode
    data['hash'] = get_hash("{}+{}".format(cardlist, gridcode), 10)
    return render_template('spymaster.html', **data)

# Helper Funcions

def get_hash(mystring, len=10):
    return hashlib.md5(mystring.encode('utf-8'))\
               .hexdigest()[:len].upper()


if __name__ == '__main__':
    app.run(debug=True)
