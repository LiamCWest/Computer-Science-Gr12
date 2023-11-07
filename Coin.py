import random

class Coin:
    def __init__(self, flip = False):
        self.side = "heads"
        if flip: self.Flip()
        
    def Flip(self):
        self.side = "heads" if random.randint(0,1) == 0 else "tails"
        
