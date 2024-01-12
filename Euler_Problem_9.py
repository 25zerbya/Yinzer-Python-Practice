#have to find pythagorean triplet s.t. a + b + c = 1000 

import itertools

combinations_list = []

def combination_gen(m, n):
    combinations = itertools.combinations(m,n)
    for combination in combinations:
        #combinations_list.append(combination)
        if combination[0] + combination[1] + combination[2] == 1000:
            yield combination    

nums = range(1,1001)
combination_size = 3
for combination in combination_gen(nums, combination_size):
    print(combination)
    if ((combination[0])**2) + ((combination[1])**2) == ((combination[2])**2):
        print(combination, "works!")
        print("the product of these three numbers is", combination[0]*combination[1]*combination[2])
        break

        
