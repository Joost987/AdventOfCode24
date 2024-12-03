file=open("day2input.txt")
biglist=[]
for line in file:
    biglist.append(list(map(int,line.split())))

def IsSafe(list):
    for i in range(1,len(list)):
        if ((list[0]-list[1]>0) != (list[i-1]-list[i]>0)) or (not 3>=abs(list[i]-list[i-1])>=1):
            return False
    return True

def IsSafePart2(list):
    if IsSafe(list): return True
    else: 
        for i in range(len(list)):
            list2=list.copy()
            list2.pop(i)
            if IsSafe(list2):
                return True
        return False

        
total1=sum(list(map(IsSafe,biglist)))
print(total1)

total2=sum(list(map(IsSafePart2,biglist)))
print(total2)
