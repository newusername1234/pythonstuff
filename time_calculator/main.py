from time_calculator import add_time
from unittest import main

print('This program will take a start time and duration\nand show the resulting time')

while True:
    start = input('Choose a start time. ex: 3:10 AM\n')
    to_add = input('Choose a duration of hours and minutes. ex: 120:30\n')
    day = input('Optionally choose a day to start on. ex: saturday\n')
    print(add_time(start,to_add,day))
    loop = input('Continue? [Y/n]\n')
    if len(loop) < 1 or 'y' in loop.lower():
        print('\n'*100)
        continue
    break
# Returns: 6:10 PM


# main(module='test_module.py',exit=False)
