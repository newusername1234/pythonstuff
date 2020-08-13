from math import pi

# enter a number and generate pi to n decimal places
def pi_to_n(n):
    return f'%.{n}f' % pi

print(pi_to_n(20))