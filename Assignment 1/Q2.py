#x=eval(input("Enter List"))
import enum
from itertools import count
import random
allin=[]
for i in range(21):
    casino=random.randint(1,100)
    allin.append(casino)
print("Average is ", sum(allin)/len(allin))
allin.sort()
maximum=max(allin)
print(maximum)
print(min(allin))
print(allin)
print(allin[-2])
print(allin[1])
'''for i in range(21):
    second=0
    if allin[i]>allin[i-1] :
        second=allin[i]
        if max(allin)>allin[i]&&allin[i]<second:'''


'''x=(1,2,3,4,5,6,7)
print(x)
print(type(x))
print(x[0])
y=list(x)
print(y)
print(sum(y))
print(min(y))
print(max(y))
print(y.count)'''