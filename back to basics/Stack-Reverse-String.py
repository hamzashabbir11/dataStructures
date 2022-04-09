A='HamzaShabbirisCool'
stack_Memory=[]
Reverse_stack=[]
b=''
for i in range(len(A)):   # pushing into stack 
    stack_Memory.append(A[i])

print(stack_Memory)

for i in range(len(stack_Memory)):  # popping from stack 

    Reverse_stack.append(stack_Memory.pop())
     
print(stack_Memory)
print(Reverse_stack)
b=b.join(Reverse_stack)
print(b)
c=b+'933839'
print(c)
dummy=[]

for i in range(len(c)):
    dummy.append(c[i])

print(dummy)

final=''




for i in range(3,len(dummy),4):
    dummy[i]='_'

final=final.join(dummy)
print(dummy)
print(final)
