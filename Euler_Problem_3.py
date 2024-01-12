
def primefactorization(x):
    i = 2
    factor_list = []

    while x/i > 2:
        if x % i:
            i += 1
        else: 
            x //= i
            factor_list.append(i)
    if x > 1:
        factor_list.append(x)
    return factor_list


print(primefactorization(600851475143))




