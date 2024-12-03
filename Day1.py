file=open("day1input.txt")
numbers1=[]
numbers2=[]
for line in file:
    numbers1.append(line.split()[0])
    numbers2.append(line.split()[1])

numbers2.sort()
numbers1.sort()
import numpy as np
numbers2=np.array(numbers2,dtype="int32")
numbers1=np.array(numbers1,dtype="int32")

total=0
for number in numbers1:
    total+=np.sum(numbers2==number)*number
print(total)
print(np.sum(np.abs(numbers2-numbers1)))
