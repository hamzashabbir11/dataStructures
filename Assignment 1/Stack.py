A='Hamza Shabbir'
stack_Memory=[]
Reverse_stack=[]
b=''

print(len(A))
for i in range(len(A)):   # pushing into stack 
    stack_Memory.append(A[i])

print(stack_Memory)

for i in range(len(stack_Memory)):  # popping from stack 

    Reverse_stack.append(stack_Memory.pop())
     
print(stack_Memory)
print(Reverse_stack)
b=b.join(Reverse_stack)
print(b)
