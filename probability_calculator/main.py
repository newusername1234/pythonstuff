from prob_calculator import Hat,experiment
from unittest import main

hat = Hat(black=6,red=4,green=3)
probability = experiment(
    hat=hat,
    expected_balls={'red':2,'green':1},
    num_balls_drawn=5,
    num_experiments=2000)
print(probability)
# main(module='test_module',exit=False)