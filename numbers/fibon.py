# display fibonacci sequence to n
def fibon_to_n(n):
    i = 0
    j = 1

    print(i)
    print(j)

    for num in range(n-2):
        i,j = j,i+j
        print(j)

fibon_to_n(10)