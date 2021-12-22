class AVL:
    def __init__(self,data=None):
        self.data = data
        self.lchild=None
        self.rchild=None
        self.height=1
class Queue:
    def __init__(self):
        self.li=[]
    def enqueue(self,data):
        self.li.append(data)
    def dequeue(self):
        if self.li is []:
            return []
        return self.li.pop(0)
    def __iter__(self):
        if self.li is []:
            return []
        for i in self.li:
            yield i

def preorderTraversal(root):
    if not root:
        return []
    print(root.data)
    preorderTraversal(root.lchild)
    preorderTraversal(root.rchild)

def postorderTraversal(root):
    if not root:
        return
    postorderTraversal(root.lchild)
    postorderTraversal(root.rchild)
    print(root.data)
def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.lchild)
    print(root.data)
    inorderTraversal(root.rchild)

def level_orderTraversal(root):
    if root.data is None:
        return []
    queue=Queue()
    queue.enqueue(root)
    a=[]
    while list(queue)!=[]:
        node=queue.dequeue()
        a.append(node.data)
        if node.lchild:
            queue.enqueue(node.lchild)
        if node.rchild:
            queue.enqueue(node.rchild)
    return a
def search(root,data,level=0):
    if root.data==data:
        return f"element found at le{level}"
    elif data<=root.data:
        if root.lchild:
            return search(root.lchild,data,level+1)
    else:
        if root.rchild:
            return search(root.rchild,data,level+1)
    return 'element not found'
def getHeight(root):
    if root==None:
        return 0
    return root.height

def rightRotate(displacedNode):
    newroot=displacedNode.lchild
    displacedNode.lchild=displacedNode.lchild.rchild
    newroot.rchild=displacedNode
    displacedNode.height=1+max(getHeight(displacedNode.lchild),getHeight(displacedNode.rchild))
    print(f"displacedNode.height=={displacedNode.height}")
    newroot.height=1+max(getHeight(newroot.rchild),getHeight(newroot.lchild))
    print(f"newroot.height=={newroot.height}")
    return newroot
def leftrotate(displacedNode):
    newroot=displacedNode.rchild
    displacedNode.rchild=displacedNode.rchild.lchild
    newroot.lchild=displacedNode
    displacedNode.height=1+max(getHeight(displacedNode.lchild),getHeight(displacedNode.rchild))
    print(f"displacedNode.height=={displacedNode.height}")
    newroot.height=1+max(getHeight(newroot.rchild),getHeight(newroot.lchild))
    print(f"newroot.height=={newroot.height}")
    return newroot
def getBalance(displacedNode):
    if not root:
        return 0
    return getHeight(displacedNode.lchild)-getHeight(displacedNode.rchild)

def insert_node(root,data):
    print(f"root1==={root}")
    if not root:
        return AVL(data)
    elif data<root.data:
        root.lchild=insert_node(root.lchild,data)
    else:
        root.rchild=insert_node(root.rchild,data)
    print(f"data=={data}")
    print(f"height of lchild=={getHeight(root.lchild)}")
    print(f" height of rchild=={getHeight(root.rchild)}")
    root.height=1+max(getHeight(root.lchild),getHeight(root.rchild))
    print(f"root.height=={root.height}")
    balance=getBalance(root)
    print(f"balance=={balance}")
    print(f"current root.data=={root.data}")
    if balance>1 and data<root.lchild.data:#Left left condition
        print("LL")
        return rightRotate(root)
    if balance>1 and data>root.lchild.data:#left right condition
        print('LR')
        root.lchild=leftrotate(root.lchild)
        return rightRotate(root)
    if balance <-1 and data>root.rchild.data:#right right condition
        print("RR")
        return leftrotate(root)
    if balance<-1 and data<root.rchild.data:#Right left condition
        root.rchild=leftrotate(root.rchild)
        print("RL")
        return leftrotate(root)
    return root
def getMinValue(root):
    if root is None or root.lchild is None:
        return root
    return getMinValue(root.lchild)
def delete_node(root,data):
    if not root:
        return root
    elif data<root.data:
        root.lchild=delete_node(root.lchild,data)
    elif data>root.data:
        root.rchild=delete_node(root.rchild,data)
    else:
        if root.lchild is None:
            temp=root.rchild
            root=None
            return temp
        if root.rchild is None:
            temp=root.lchild
            root=None
            return temp
        temp=getMinValue(root.rchild)
        root.data=temp.data
        root.rchild=delete_node(root.rchild,temp.data)
        #rotation required
    root.height=1+max(getHeight(root.lchild),getHeight(root.rchild))
    balance=getBalance(root)
    if balance>1 and getBalance(root.lchild)>=0:
        return rightRotate(root)
    if balance<-1 and getBalance(root.rchild)<=0:
        return leftrotate(root)
    if balance>1 and getBalance(root.lchild)<=0:
        root.lchild=leftrotate(root.lchild)
        return rightRotate(root)
    if balance<-1 and getBalance(root.rchild)>=0:
        root.rchild=rightRotate(root.rchild)
        return leftrotate(root)
    return root
def delete_all_node(root):
    root.data=root.rchild=root.lchild=None
root=AVL(5)
# print("Inorder Traversal is ")
# inorderTraversal(root)
# print("postorderTraversal is")
postorderTraversal(root)
root=insert_node(root,10)
root=insert_node(root,15)
root=insert_node(root,20)
root=delete_node(root,15)
# delete_all_node(root)
print("Level order traversal is")
print(level_orderTraversal(root))