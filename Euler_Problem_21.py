
def d(n):
    factors = []
    for x in range(1, (n//2) + 1):
        if n % x == 0:
            factors.append(x)
    # print(factors))
    corn = sum(factors)
    return corn

bigsum = 0
for x in range(1, 10001):
    test1 = d(x)
    test2 = d(test1)
    if x == test2 and test1 != test2:
        print(test1, test2)
        bigsum += (test1 + test2)
        print(bigsum)

realsum = bigsum / 2
print(realsum)
    






    

