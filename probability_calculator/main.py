from prob_calculator import Hat,experiment
from unittest import main

hat = Hat(black=9,red=1)
probability = experiment(
    hat=hat,
    expected_balls={'red':1},
    num_balls_drawn=1,
    num_experiments=2000)
print(probability)
# main(module='test_module',exit=False)