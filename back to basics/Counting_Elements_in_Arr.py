'''arr=[]
arr=input("Enter Numbers in your Array")
print(arr)
print(len(arr))'''

"""Times=0
l=[1,2,3,4,5,5,5]

for i in range(len(l)):
    if l[i]==5:
        Times=Times+1
print(Times)   """

l=[1,2,3,4,5,5,5]
Times=0
for i in range(len(l)):
    if l[i]==5:
        Times=Times+1
if Times>0:
    print('yes')
else:
    print('no')
print('Five is Present for these many times ', Times)   
r=len(l)+1
e=[]
for i in range(1,r):
    print(l[-i])
    e.append(l[-i])

print('Reverse list is', e)
#
    
    



