def gen_primes(n):
        
        def is_prime(n):
            for num in range(2,n):
                if n != 2 and n % num == 0:
                    return False
            return True

        for num in range(2,n):
            if is_prime(num):
                yield num

n = 3

while True:
    x = gen_primes(n)
    play = input('[continue/stop]? ')
    if not 'stop' in play:
        print(next(x))
        n += 1