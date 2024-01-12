pnums = [2,3]
x = 5 #<- starting num
while pnums[-1] < 2000000:
    isprime = True
    for i in pnums: # <-- i is supposed to be running through each of the prime numbers as divisors
        if i * i > x:
            break
        if x % i == 0:
            isprime = False
            break
    if isprime == True:
        pnums.append(x)
        print(x)
    x += 2
    
print(sum(pnums[:-1]))