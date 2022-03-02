# Circular List 
l=[1,2,3,4,5]
l_copy=l
b=l_copy[1]
#l[0]=l[-1]
a=len(l)
#for i in range(1,a):

buffer=l[1]
l[0]=l[-1]
l[4]=l[3]
l[3]=l[2]
l[2]=l[1]
l[1]=l[0]

print(l)

