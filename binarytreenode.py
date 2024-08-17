class Treenode:
    def __init__(self,data):
        self.data=data
        self.rightnode=None
        self.leftnode=None

def insert(root,data):
    if root==None:
        return Treenode(data)
    if root.data > data:
        root.leftnode=insert(root.leftnode,data) 
    else: 
        root.rightnode=insert(root.rightnode,data)
    return root

def search(root,val):
    if root.data==val:
        return root 
    elif root.data>val and root.leftnode is not None:
        return search(root.leftnode,val)
    elif root.data<val and root.rightnode is not None:
        return search(root.rightnode,val)
    else: 
        return -1 
    
def inOrder(root): # left, root, right
    if root.data is not None:
        if root.leftnode is not None:
            inOrder(root.leftnode)
        print(root.data)
        if root.rightnode is not None:
            inOrder(root.rightnode)

def preOrder(root): # root, left, right
    if root.data is not None:
        preOrder(root.data)
        if root.leftnode is not None:
            preOrder(root.leftnode)
        print(root.data)
        if root.rightnode is not None:
            preOrder(root.rightnode)


num=int(input("What's the max elements you want for your tree?:"))

root=None 

for i in range(num):
    d=int(input("Enter the data for the node:"))
    root=insert(root,d)

inOrder(root)

snum=int(input("Which number do you want to search for?"))

keynode=search(root,snum)
 
if keynode==-1:
    print("Number was not found!")
else:
    print("They key exists!:",keynode.data )





    
