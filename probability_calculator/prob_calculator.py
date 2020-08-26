import copy
import random
from collections import defaultdict

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for key,value in kwargs.items():
            for n in range(0,value):
                self.contents.append(key)
    
    def draw(self,to_draw):
        drawn = []
        if to_draw >= len(self.contents):
            drawn = self.contents
            self.contents = []
            return drawn
        for x in range(0,to_draw):
            i = random.randint(0,len(self.contents)-1)
            drawn.append(self.contents.pop(i))
        return drawn

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    successes = 0
    for n in range(0,num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn = defaultdict(lambda: 0)
        for ball in new_hat.draw(num_balls_drawn):
            drawn[ball] += 1
        for key,value in expected_balls.items():
            if drawn[key] < value:
                break
            successes += 1
    probability = (successes/num_experiments)*100
    return f'{round(probability,2)}%'