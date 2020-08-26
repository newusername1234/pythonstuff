import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for key,value in kwargs.items():
            for n in range(0,value):
                self.contents.append(key)
    
    def draw(self,to_draw):
        if to_draw >= len(self.contents):
            return self.contents
        drawn = []
        for x in range(0,to_draw):
            i = random.randint(0,len(self.contents)-1)
            drawn.append(self.contents.pop(i))
        return drawn

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    new_hat = copy.copy(hat)
    