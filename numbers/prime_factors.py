# take input and display all prime factors if any

def get_prime_factors(n):
            
    def gen_primes(n):
        
        def is_prime(n):
            for num in range(2,n):
                if n != 2 and n % num == 0:
                    return False
            return True

        for num in range(2,n):
            if is_prime(num):
                yield num
        
    possible_factors = gen_primes(num)
    

    if n == 1:    
        return 1

    else:
        try:
            factor = next(possible_factors)
            
            while n % factor != 0:
                factor = next(possible_factors)
            
            print(factor)
            get_prime_factors(n/factor)

        except StopIteration:
            print(f'{n} has no prime factors')

num = int(input('Find prime factors for: '))

get_prime_factors(num)