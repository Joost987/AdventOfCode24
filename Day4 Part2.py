import re
import numpy as np
file=open("day4input.txt")
#file=open("day4example.txt")


biglist=[]
for line in file:
    biglist.append(list(line.split()[0]))
biglist=np.array(biglist)
#print(biglist[0])


def FindXMAS2(biglist):
    matchAs=[]
    for (i,lst) in enumerate(biglist):
        for match in re.finditer("MAS","".join(lst)):
            if (i-match.span()[0])%(len(lst))>=2 and match.span()[0]<=len(lst)-3:
                matchAs.append((match.span()[0]+1,(i-match.span()[0]-1)%len(lst)))
        for match in re.finditer("SAM","".join(lst)):
            if (i-match.span()[0])%(len(lst))>=2 and match.span()[0]<=len(lst)-3:
                matchAs.append((match.span()[0]+1,(i-match.span()[0]-1)%len(lst)))
    return matchAs

def FindXMAS3(biglist):
    matchAs=[]
    for (i,lst) in enumerate(biglist):
        for match in re.finditer("MAS","".join(lst)):
            if (i+match.span()[0])%(len(lst))<=len(lst)-3 and match.span()[0]<=len(lst)-3:
                matchAs.append((match.span()[0]+1,(i+match.span()[0]+1)%(len(lst))))
        for match in re.finditer("SAM","".join(lst)):
            if (i+match.span()[0])%(len(lst))<=len(lst)-3 and match.span()[0]<=len(lst)-3:
                matchAs.append((match.span()[0]+1,(i+match.span()[0]+1)%(len(lst))))
    return matchAs


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
matchA2=FindXMAS2(np.transpose(biglist2))
matchA3=FindXMAS3(np.transpose(biglist3))
#print(len(matchA2),len(matchA3))
#print(matchA2)
#print(matchA3)
print(len(set(matchA2).intersection(set(matchA3))))