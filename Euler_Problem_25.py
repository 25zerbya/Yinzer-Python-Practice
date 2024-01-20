Flist = [1,1]
F1, F2 = 0, 1 # sets both addend indexes
while ((Flist[-1])/(10**999)) <= 1:  # there are two initial approaches I could have taken: take the Flist[-1] and converted it to a string
    Fnew = Flist[F1] + Flist[F2]     # OR do a sort a numerical check on whether Flist[-1] has 1000 digits. 10**999 has exactly 1000 digits
    Flist.append(Fnew)               # dividing by 10**999 will only give 1 or greater to another number with 1000 digits or more!
    F1, F2 = F1 + 1, F2 + 1 # moves both addend indexes forward one
print(len(Flist))
# the numerical check seemed a lot faster, and it was!
# Tuples are useful...just be careful andrew
    
