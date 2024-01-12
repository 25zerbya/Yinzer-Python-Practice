# find the sum of even valued fibonacci numbers w/ value below 4,000,000

F_1 = 1
F_2 = 2
total = 2
#Fibonacci_num_2 = 2
#print (F_1)
#print (F_2)
while F_2 + F_1 < 4000000:
    F_1 =  F_1 + F_2 # F_1 = 1 + 2 = 3!!
    F_2 = F_1 + F_2 # F_2 = 3 + 2 = 5!!
    if F_1 % 2 == 0:
        total += F_1
    if F_2 % 2 == 0:
        total += F_2
    
print(total)






    
    
    
