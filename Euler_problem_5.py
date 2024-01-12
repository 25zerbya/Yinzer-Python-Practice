#goal: find the lowest number that can be divided by 1-20 evenly
def gcd(x,y):

    if x == y:
        return x
    if x > y:
        count = x-1
        while count >= 1:
            if x % count == 0 and y % count == 0:
                return count
                break
            else:
                count -= 1
        count -= 1             
    if y > x:
        count = y-1
        while count >= 1:
            if x % count == 0 and y % count == 0:
                return count
                break
            else:
                count -= 1
        count -= 1

def lcm(a,b):
    return abs(a * b) // gcd(a, b)


def cum(n):
    b = 1
    for i in range(1, n + 1):
        b = lcm(b, i)
        print(b)
    return b


die = cum(20)
print(die)



