import pandas as pd
import numpy as np
import random

class NameCards():

    names_file = 'lib/words2.txt'

    def __init__(self):
        self.names = open(self.names_file, 'r').readlines()
        self.grid = pd.DataFrame(index=pd.MultiIndex.from_product(
            [range(5), range(5)])
        )

    def draw_cards(self, n=25):
        self.cards = random.sample(self.names, n)
        random.shuffle(self.cards) # For good measure
        self.grid['card'] = self.cards
        self.cardlist = '_'.join([card.strip().upper() for card in self.cards])

    def clone_cards(self, cardlist):
        self.grid['card'] = cardlist.split('_')
        self.cardlist = cardlist


class KeyCard():

    params = {
        'red': 8,
        'blue': 8,
        'double': 1,
        'neutral': 7,
        'assassin': 1
    }
    
    codes = {
        'r':'red',
        'b':'blue',
        'a':'assassin',
        'n':'neutral'
    }

    teams = {'red','blue'}

    def __init__(self):
        
        # Create grid
        self.grid = pd.DataFrame(index=pd.MultiIndex.from_product(
            [range(5),range(5)])
            )

    def draw_card(self):       
        
        # Pick starting team
        self.team = random.sample(self.teams, 1)[0]
        
        # Get cards
        self.cards = []
        for ctype in self.params.keys():
            for n in range(self.params[ctype]):
                if ctype == 'double':
                    ctype = self.team
                self.cards.append(ctype)

        # Shuffle cards
        random.shuffle(self.cards)
        
        # Bind to dataframe
        self.grid['card'] = self.cards
        
        # Generate grid code
        self.gridcode = ''.join([x[0][0] for x in self.cards])
        self.gridcode = self.team[0] + self.gridcode
    
    def clone_card(self, gridcode):
        
        self.team = self.codes[gridcode[:1]]
        self.grid['card'] = [self.codes[x] for x in gridcode[1:]]
        self.gridcode = gridcode
        
        
    