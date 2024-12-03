import re
file=open("day3input.txt")
lst=[]
for line in file:
    lst.append(line)

liststring="".join(lst)
matches=re.findall("mul\(\d+,\d+\)",liststring)
total=0
for match in matches:
    numbers=re.findall("\d+",match)
    total+=int(numbers[0])*int(numbers[1])
print(total)

#part2
total=0
matches2=re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)",liststring)
do=True
for match in matches2:
    if match=="don't()":
        do=False
    elif match=="do()":
        do=True
    elif do and "mul" in match:
        numbers=re.findall("\d+",match)
        total+=int(numbers[0])*int(numbers[1])

print(total)