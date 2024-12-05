import re
import numpy as np
file=open("day4input.txt")
#file=open("day4example.txt")

biglist=[]
for line in file:
    biglist.append(list(line.split()[0]))
biglist=np.array(biglist)
print(biglist[0])


def FindXMAS(biglist,total):
    for lst in biglist:
        total+=len(re.findall("XMAS","".join(lst)))
        total+=len(re.findall("SAMX","".join(lst)))
    print(total)
    return total

def FindXMAS2(biglist,total):
    for (i,lst) in enumerate(biglist):
        for match in re.finditer("XMAS","".join(lst)):
            #index=(match.span()[0]-i)%(len(lst))
            if (i-match.span()[0])%(len(lst))>=3 and match.span()[0]<=len(lst)-4:
                total+=1
            else: print(i,match)
        for match in re.finditer("SAMX","".join(lst)):
           # index=(match.span()[0]-i)%(len(lst))
            if (i-match.span()[0])%(len(lst))>=3 and match.span()[0]<=len(lst)-4:
                total+=1
            else: print(match,"a",i,(i-match.span()[0])%(len(lst))>=3)
    print(total)
    return total

def FindXMAS3(biglist,total):
    for (i,lst) in enumerate(biglist):
        for match in re.finditer("XMAS","".join(lst)):
           # index=(match.span()[0]+i)%(len(lst))
            if (i+match.span()[0])%(len(lst))<=len(lst)-4 and match.span()[0]<=len(lst)-4:
                total+=1
        for match in re.finditer("SAMX","".join(lst)):
           # index=(match.span()[0]+i)%(len(lst))
            if (i+match.span()[0])%(len(lst))<=len(lst)-4 and match.span()[0]<=len(lst)-4:
                total+=1
    print(total)
    return total


total=FindXMAS(biglist,0)
#print(total)
total=FindXMAS(np.transpose(biglist),total)
#print(total)
biglist2=[]
biglist3=[]
for (i,lst) in enumerate(biglist):
    biglist2.append(np.roll(lst,i))
    biglist3.append(np.roll(lst,-i))

biglist2=np.array(biglist2) #shifted to the righ
biglist3=np.array(biglist3) #shifted to the left so finds diagonals running right and down
#print(biglist)
#print(biglist2)

#print(np.transpose(biglist))
#print(np.transpose(biglist2))
total=FindXMAS2(np.transpose(biglist2),total)
total=FindXMAS3(np.transpose(biglist3),total)
print(biglist.shape)
print(total)