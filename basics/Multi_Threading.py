import threading
import time
def func():
    for i in range(200000):
            
        print('Hello\n')
        time.sleep(0.1)

def func_2():
    for i in range(200000):
            
        print('Hello from 2nd Function\n')
        time.sleep(0.1)


t1=threading.Thread(target=func)
t2=threading.Thread(target=func_2)
t1.start()
t2.start()
t1.join()
print('T1 ended')
t2.join()
print("End")
print('End')


'''def func():
    while(1):
            
        print('Hello\n')
        time.sleep(0.5)

def func_2():
    while(1):
            
        print('Hello from 2nd Function\n')
        time.sleep(2)


t1=threading.Thread(target=func)
t2=threading.Thread(target=func_2)
t1.start()
t2.start()
t1.join()
t2.join()
print("End")'''