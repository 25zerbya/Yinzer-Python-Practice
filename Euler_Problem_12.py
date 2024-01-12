#ok so first we have to create a bunch of triangle numbers
def factorize(n):
    factors = [1]

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    return factors

trianglenums = [1]

x = 0

while len(factorize(trianglenums[-1])) <= 500:
    triangle = trianglenums[x] + (x+2)
    trianglenums.append(triangle)
    print(trianglenums[-1])
    x += 1

print(trianglenums[-1])

#print(trianglenums)
#print(len(trianglenums))
