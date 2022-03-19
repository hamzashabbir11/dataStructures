import requests 

class Node():
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    
class LinkList():
    def __init__(self) -> None:
        self.head=None

link_list1=LinkList()

node1=Node(1)
node2=Node(2)
node3=Node(3)

link_list1.head=node1
link_list1.head.next=node2
link_list1.head.next.next=node3

print(link_list1.head.data)
print(link_list1.head.next.data)
print(link_list1.head.next.next.data)

'''url='https://www.google.com/'
resp=requests.get(url)
print(resp.status_code)
print(resp.elapsed)
print(resp.cookies)'''