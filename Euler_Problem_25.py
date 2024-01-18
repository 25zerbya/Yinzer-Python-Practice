Flist = [1,1]

F1 = 0
F2 = 1

while ((Flist[-1])/(10**999)) <= 1:
    Fnew = Flist[F1] + Flist[F2]
    Flist.append(Fnew)
    F1 += 1
    F2 += 1

print(len(Flist) - 1)
    