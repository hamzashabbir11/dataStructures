numm=6
l=[]
for i in range(1,numm+1):
    l.append(numm%i)

for i in range(1,len(l)-1):
    if l[i] ==0:
        print('not prime')

print(l)


'''
print(numm%1)
print(numm%2)
print(numm%3)
print(numm%4)
print(numm%5)
#l[0] & l[end] always 0 
# agr l[1]:l[end-1] any 0 so ==> not prime'''
      
        

            
        
