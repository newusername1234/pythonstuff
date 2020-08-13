from math import e

def e_to_n(n):
    return f'%.{n}f' % e

print(e_to_n(3))