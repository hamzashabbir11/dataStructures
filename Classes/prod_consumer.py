import time
order_producer=['Pizza','McCrispy','McFries','Crosoint','Latte','Club Sandwitch','French Toast','Steak','Milk Shake','Cake']
order=[]
j=0
i=0

while(i<len(order_producer)):
    order.insert(i,order_producer[i])
    print(order[i])
    time.sleep(0.5)
    i=i+1

serve=[]

print('Your Order is Preparing ')
while(j<len(order)):
    print(order.pop(j))
    time.sleep(2)
    
    

print(order)






