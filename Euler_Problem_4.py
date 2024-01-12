products = []

def multiply(z):
    
    col1 = list(range(100, z))
    col2 = list(range(100, z))
    
    y = 0

    while y < z-100:
        x = 0
        while x + y < z-100:
            mult = col1[x + y] * col2[y]
            #print(mult)
            products.append(mult)
            x += 1
        y += 1
    products.sort()
    #print(products)


multiply(1000)

def sorting(n):

    palindromes = []

    strings = [str(item) for item in products]
    #print(strings)
    x = 0 #<-- counter var for string
    while x < len(strings):
        testnum = strings[x] # <-- establish a testing variable to run through each item in list. 
        
        y = 0 # <-- counter var for first char in string
        z = len(testnum) - 1  # <-- counter var for last char in string

        while z - y >= -1: # <--- ensures that counter vars don't eclipse eachother/makes sure they stop at middle
                
            if testnum[y] == testnum[z]: #<-- if character 1 is equal to last character, print - if not, move to next
                #print(testnum)
                
                if z-y <= 0: # <-- ok are the counters the same or eclipsed? yes: its a palindrome add to list, STOP, and move to next - no: move closer. 
                         palindromes.append(testnum)
                         x += 1
                         break
                else:
                     y += 1
                     z -= 1          
            else:
                x +=1
                break

        x += 1
    palindrome_list = [int(x) for x in palindromes]
    palindrome_list.sort()
    print(palindrome_list)

sorting(products)






