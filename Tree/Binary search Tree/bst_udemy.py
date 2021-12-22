class BST:
    def __init__(self,data=None):#Time and space complexity is O(1)
        self.data = data
        self.lchild=None
        self.rchild=None
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if self.queue ==[]:
            return 0
        else:
            return self.queue.pop(0)
    def __iter__(self):
        for i in self.queue:
            yield i

def insert(root,data):#Time complexity is O(logn)
    if root.data is None:
        root.data=data
    elif data<=root.data:
        if root.lchild is None:
            root.lchild=BST(data)
        else:
            insert(root.lchild,data)
    else:
        if root.rchild is None:
            root.rchild=BST(data)
        else:
            insert(root.rchild,data)
    return 'Node inserted successfully'

def preorderTraversal(root):#Time complexity complexity
    if not root:
        return 'Nothing to preorder'
    print(root.data)
    preorderTraversal(root.lchild)
    preorderTraversal(root.rchild)

def inorderTraversal(root):
    if not root:
        return 'Nothing to inorder'
    inorderTraversal(root.lchild)
    print(root.data)
    inorderTraversal(root.rchild)
def postorderTraversal(root):
    if not root:
        return "Nothing to postorderTraversal"
    postorderTraversal(root.lchild)
    postorderTraversal(root.rchild)
    print(root.data)

def level_orderTraversal(root):
    if not root:
        return 'Nothing to Traversal'
    queue=Queue()
    queue.enqueue(root)
    while list(queue)!=[]:
        node=queue.dequeue()
        print(node.data)
        if node.lchild:
            queue.enqueue(node.lchild)
        if node.rchild:
            queue.enqueue(node.rchild)
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
def min_node(root):
    if not root:
        return 'Nothing to find minimum'
    ptr=root
    while(ptr.lchild!=None):
        ptr=ptr.lchild
    return ptr
def max_node(root):
    if not root:
        return 'Nothing to find minimum'
    ptr1=root
    while(ptr1.rchild!=None):
        ptr1=ptr1.rchild
    return ptr1.data

def delete_node(root,data):
    if root is None:
        return root
    if data<root.data:
        root.lchild=delete_node(root.lchild,data)
    elif data>root.data:
        root.rchild=delete_node(root.rchild,data)
    else:           #one child condition
        if root.lchild is None:
            temp=root.rchild
            root=None
            return temp
        if root.rchild is None:
            temp=root.rchild
            root=None
            return temp
        temp=min_node(root.rchild)
        root.data=temp.data
        root.rchild=delete_node(root.rchild,temp.data)
    return root

def delete_BST():
    root.data=root.lchild=root.rchild=None
    return 'BST deleted successfully'


root=BST()
li=[70,50,80,10,20,100]
for i in li:
    print(insert(root,i))
print("preorder_traversal is ")
preorderTraversal(root)
print("inorder traversal is ")
inorderTraversal(root)
print("postorder_traversal is ")
postorderTraversal(root)
print(search(root,130))
print(f"minimum node is {min_node(root)}")
print(f"maximum node is {max_node(root)}")
print("postorder_traversal is ")
postorderTraversal(root)
print("Level order traversal")
level_orderTraversal(root)
print(delete_node(root,20))
# print(delete_BST())
print("Level order traversal")
level_orderTraversal(root)
