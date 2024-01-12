#longest collatz sequence w numbers under 1 million

lengths = {}

for x in range(2, 1000001):
    y = 1 #<-- counting var
    first_x = x
    while x != 1:
        if x in lengths:
            y += lengths[x] - 1
            break

        if x % 2 == 0:
            x = x // 2
        else:
            x = (3*x) + 1
        y += 1
        
    lengths[first_x] = y 

print(lengths)

maxlength = max(lengths, key=lambda k: lengths[k])

# maxlength_index = lengths.index(maxlengthsequence) + 1 #<-- have to increase index num by one in order for it to match number
# #if max of the lengths is, let's say, arbirtrarily 1000, and it happens when x = 3, it's going to be the third item in the 
# #lengths list. if we index that, the index is going to = 2

print("the number with the longest collatz sequence is", maxlength,'!')







        