#

def dif(n):
    whole_square = ((n + 1) * (n / 2))**2
    print(whole_square)
    sum = 0
    for i in range(1, n+1):
        squ = i**2
        sum = sum + squ
        print(sum)
    total = whole_square - sum
    return total

done = dif(100)
print(done)