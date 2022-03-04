# Circular List 
from copy import copy, deepcopy
l=[1,2,3,4,5,6,7]
#A=l.copy()
A=deepcopy(l)
a=len(l)
l[0]=A[-1]
for i in range(1,a):
    l[i]=A[i-1]

    
print(l)



