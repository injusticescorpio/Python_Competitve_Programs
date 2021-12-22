class Tree:
    def __init__(self,size):#Time complexity O(1) and space complexity O(n)
        self.li=[None]*size
        self.lastusedindex=0
        self.maxsize=size
    def insertNode(self,value):#Time and space is O(1)
        print(f"self.lastusedindex={self.lastusedindex}")
        if self.lastusedindex+1==self.maxsize:
            print("Binary Tree is Full")
        self.li[self.lastusedindex+1]=value
        self.lastusedindex+=1
        return("Value inserted successfully")
    def search(self,data):#Time is O(n) and search is O(n)
        for i in self.li:
            if i==data:
                return("Node found at Binary Tree")
        return "Node not found"
    def preorder_traversal(self,index=1):
        if index>self.lastusedindex:
            return
        print(self.li[index])
        self.preorder_traversal(index*2)
        self.preorder_traversal(index*2+1)
    def postorder_traversal(self,index=1):#Time and space complexity is O(n)
        if index>self.lastusedindex:
            return
        self.preorder_traversal(index*2)
        self.preorder_traversal(index*2+1)
        print(self.li[index])
    def inorder_traversal(self,index=1):
        if index>self.lastusedindex:
            return
        self.preorder_traversal(index * 2)
        print(self.li[index])
        self.preorder_traversal(index * 2 + 1)
    def level_order_traversal(self):
        # print(self.li)
        for i in range(1,self.maxsize):
            if self.li[i]==None:
                break
            else:
                print(self.li[i])
    def delete_Node(self,value):#time and space complexity is O(n)
        if self.lastusedindex==0:
            return "Nothing to delete"
        for i in range(1,self.lastusedindex):
            if self.li[i]==value:
                self.li[i]=self.li[self.lastusedindex]
                self.li[self.lastusedindex]=None
                self.lastusedindex-=1
                return "Node deleted"
        return "No element found"
    def delete_Tree(self):
        if self.li ==[]:
            return "Already deleted"
        self.li=[None]*self.maxsize
        self.lastusedindex=0
        return "Tree deleted"



BinaryTree=Tree(10)
print(BinaryTree.insertNode('Drinks'))
print(BinaryTree.insertNode('Tea'))
print(BinaryTree.insertNode('Cold'))
print(BinaryTree.insertNode('Coffee'))
print(BinaryTree.insertNode('Ripple'))
print(BinaryTree.search('Tea1'))
print("preorder_traversal is")
BinaryTree.preorder_traversal()
print("inorder traversal is")
BinaryTree.inorder_traversal()
print("postorder_traversal traversal is")
BinaryTree.postorder_traversal()
print("level_traversal traversal is")
BinaryTree.level_order_traversal()
print(BinaryTree.delete_Tree())
print(BinaryTree.insertNode('Drinks'))
print(BinaryTree.insertNode('Tea'))
print("level_traversal traversal is")
BinaryTree.level_order_traversal()
print("inorder traversal is")
BinaryTree.inorder_traversal()