import threading
import time
order_producer=['Pizza','McCrispy','McFries','Crosont','Doughnut']
order=[]
j=0
i=0
serve=[]

      
while(i<len(order_producer)):
        order.insert(i,order_producer[i])
        print(order[i])
        time.sleep(0.5)
        i=i+1

      
print('Your Order is Preparing ')
while(j<len(order)):
    print(order.pop(j))
    time.sleep(2)


print(order)






