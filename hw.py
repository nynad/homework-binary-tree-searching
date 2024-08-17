
class Treenode:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None 
        

def inOrder(root):
    if root.leftnode != None:
        inOrder(root.leftnode)

    print(root.data)
    if root.rightnode!=None:
        inOrder(root.rightnode)

def preOrder(root):
    print(root.data)
    if root.leftnode != None:
        preOrder(root.leftnode)

    if root.rightnode !=None:
        preOrder(root.rightnode)
    
def postOrder(root):
    if root.leftnode != None:
        postOrder(root.leftnode)
        
    if root.rightnode != None:
        postOrder(root.rightnode)

    print(root.data)


def menu(input,name):
    input=int(input("Welcome to the Tree Creator! Enter what you would like to do.\n.0. Create a Tree\n1. Create Leftnode \n2.Create Rightnode\n3.Traverse InOrder\n4.Traverse PostOrder\n5.Traverse PreOrder"))
    if input==0:
        name=input("Enter your tree name!")

    if input==1:
        ui1=int(input("Enter the data you want the node to hold."))
        name.leftnode(ui1)

    if input==2:
        ui2=int(input("Enter the data you want the node to hold."))
        name.rightnode(ui2)

    if input==3:
        inOrder()
    
    if input==4:
        postOrder()

    if input==5:
        preOrder()


menu(input)
