#ok so first we have to calculate the number 2^1000

thenumber = 2 ** 1000

print(thenumber)

str_thenumber  = str(thenumber)

print(str_thenumber)


yummy_sum = 0

for x in range(0, len(str_thenumber)):
    str_digit = str_thenumber[x]
    digit = int(str_digit)
    yummy_sum += digit

print(yummy_sum)