filepath = '/Users/andrewzerby/downloads/0022_names.txt'
#The first step is organizing this list

with open(filepath, 'r') as file: #takes names from .txt and puts them into list?
    big_list = file.read()

# print(big_list)
str_big_list = big_list.split(',') # splits the big long string (txt file) into list of substrings. substrings are formed when ','
                                   # is detected

final = [x.strip()[1:-1] for x in str_big_list] #takes out first and last character (1:-1) of the substrings, which are the extraneous ""s
final.sort() # nice built-in sort function

# Now that the list has been sorted, we need to associate TWO values with each name
# First value: the number it is in the alphabetized list, index + 1 should take care of this
place_vals = [final.index(num) + 1 for num in final]

# Second value: the total number value of the letters (a is 1, b is 2) so BAB (fake first name, j an example) is 2 + 1 + 2 = 5
# this dictionary associates each letter in the alphabet with the correct number. Perfect!
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_dict = {num: alphabet.index(num) + 1 for num in alphabet}

name_vals = []
for x in range(0, len(final)):               # This loop just iterates through every name in the 'final' list
    running_total = 0                        # Resets name value total for each name
    chars = [char for char in final[x]]      # creates a list for the characters in each substring.                                      
    # print(chars)                             # check
    for y in range(0, len(chars)):           # this loop produces the name value
        temp_val = alphabet_dict[chars[y]]   # temp_val is the variable that holds the value associated with each letter. Iteratively extracts each val from the dictionary defined earlier around line 19
        running_total += temp_val            # running_total is the addition, happening one letter at a time, constantly updating the value until the were done with the name
    name_vals.append(running_total)          # add to a list
print(name_vals[937])

temp_prod = 1
total = 0
for x in range(0,len(name_vals)):   
    temp_prod = place_vals[x] * name_vals[x] # gives final score for each name
    total += temp_prod
print(total)







