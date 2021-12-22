class BST:
    def __init__(self,data=None):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def insertion(self,data):
        if self.data is None:
            self.data=data
        elif self.data==data:
            return
        elif self.data>data:
            if self.leftchild:
                self.leftchild.insertion(data)
            else:
                self.leftchild=BST(data)
        else:
            if self.rightchild:
                self.rightchild.insertion(data)
            else:
                self.rightchild = BST(data)
    def search(self,data,level=0):
        if self.data==None:
            print("Tree empty no element")
        elif self.data==data:
            print(f"{self.data} found at level {level}")
            return
        elif self.data>data:
            if self.leftchild:
                self.leftchild.search(data,level+1)
            else:
                print("element not found")
        else:
            if self.rightchild:
                self.rightchild.search(data, level + 1)
            else:
                print("element not found")
    def preorder(self):
        print(self.data)
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()
    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        print(self.data)
        if self.rightchild:
            self.rightchild.inorder()
    def postorder(self):
        if self.leftchild:
            self.leftchild.postorder()
        if self.rightchild:
            self.rightchild.postorder()
        print(self.data)
    def delete(self,data,root_data):
        if self.data==None:
            print("deletion not possible")
            return
        elif self.data>data:
            if self.leftchild:
                self.leftchild=self.leftchild.delete(data)
            else:
                print("data is not found")
        elif self.data<data:
            if self.rightchild:
                self.rightchild=self.rightchild.delete(data)
            else:
                print("Data not found")
        else:                           #if deleting node containing 0 or 1 or 2 child
         # Conditions for deleting node which contains 0 or 1 child
            if self.leftchild is None:
                temp = self.rightchild
                if data==root_data:
                    self.data=temp.data
                    self.leftchild=temp.leftchild
                    self.rightchild=temp.rightchild
                    temp=None
                self=None
                return temp
            if self.rightchild is None:
                temp=self.leftchild
                if data==root_data:
                    self.data=temp.data
                    self.leftchild=temp.leftchild
                    self.rightchild=temp.rightchild
                    temp=None
                self=None
                return temp
            # Conditions for deleting node which contains 2 child
            node=self.rightchild
            while node.leftchild:
                node=node.leftchild
            self.data=node.data
            self.rightchild=self.rightchild.delete(node.data)
        return self
def count(node):
    if not node:
        return 0
    else:
        return 1+count(node.leftchild)+count(node.rightchild)
        







root=BST()
l=[10,1,2]
for i in l:
    root.insertion(i)
root.search(6)
print("preorder traversal")
root.preorder()
print("Inorder traversal")
root.inorder()
print("postorder")
root.postorder()
print(f"count =={count(root)}")

##deleting root node There are 3 cases
# case 1 if root node is the left node

if count(root)>1:
    root.delete(10,root.data)
else:
    print("unable to delete data")


print("postorder")
root.postorder()









