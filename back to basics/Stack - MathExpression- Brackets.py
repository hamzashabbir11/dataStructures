steck=[]
exp_meth='[x+{(y+z)}]'
for i in range(len(exp_meth)):
    if exp_meth[i]=='[':
        steck.append('[')
    if exp_meth[i]=='{':
        steck.append('{')
    if exp_meth[i]=='(':
        steck.append('(')
    if exp_meth[i]==')':
        steck.pop()
    if exp_meth[i]=='}':
        steck.pop()
    if exp_meth[i]==']':
        steck.pop()


print(steck)
print(type(steck))
#print(exp_meth[1])
