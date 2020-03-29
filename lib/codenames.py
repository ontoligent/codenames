import pandas as pd
import numpy as np
import random

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
        
        
    