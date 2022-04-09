class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None



class LinkList:
    def __init__(self) -> None:
        self.head=None

    def insert_begin(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
        print(newnode.next)
    def insert_end(self,enddata):
        endnode=Node(enddata)
        last=self.head
        while(last.next != None):
            last=last.next
        
        last.next=endnode

         
        
LinkList1=LinkList()
Node1=Node(1)
Node2=Node(2)
Node3=Node(3)
Node4=Node(4)


LinkList1.head=Node1
LinkList1.head.next=Node2
LinkList1.head.next.next=Node3
LinkList1.head.next.next.next=Node4
LinkList1.insert_begin(5)
LinkList1.insert_end(6)


print(LinkList1.head.data)
print(LinkList1.head.next.data)
print(LinkList1.head.next.next.data)
print(LinkList1.head.next.next.next.data)
print(LinkList1.head.next.next.next.next.data)
print(LinkList1.head.next.next.next.next.next.data)








'''
import requests 
url='https://www.google.com/'
resp=requests.get(url)
print(resp.status_code)
print(resp.elapsed)
print(resp.cookies)'''