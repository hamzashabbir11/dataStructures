from logging import root


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None


root=Node(1)
root.left=Node(2)
root.right=Node(3)


print(root.data)
print(root.left.data)
print(root.right.data)
'''
     1
   /   \
  2     3 '''

root.left.left=Node(4)
root.left.right=Node(5)
print(root.left.left.data)
print(root.left.right.data)

'''
     1
   /   \
  2     3 
 / \
4   5  '''    

root.right.left=Node(6)
root.right.right=Node(7)
print(root.right.left.data)
print(root.right.right.data)


'''
      1
   /     \
  2       3 
 / \     / \
4   5   6   7        '''  
