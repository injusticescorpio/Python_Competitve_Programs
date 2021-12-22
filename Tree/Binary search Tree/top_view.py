class BST:
    def __init__(self,data=None):
        self.data=data
        self.lchild=None
        self.rchild=None

class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if self.queue==[]:
            return []
        return self.queue.pop(0)
    def __iter__(self):
        if self.queue==[]:
            return []
        for i in self.queue:
            yield i

def insert_node(root,data):
    if root.data is None:
        root.data=data
    elif data<=root.data:
        if root.lchild:
            insert_node(root.lchild,data)
        else:
            root.lchild=BST(data)
            print("Node inserted succesfully")
    else:
        if root.rchild:
            insert_node(root.rchild,data)
        else:
            root.rchild=BST(data)
            print("Node inserted succesfully")
def level_order_traversal(root):
    if not root:
        return "nothing to traverse"
    queue=Queue()
    queue.enqueue(root)
    while(list(queue)!=[]):
        node=queue.dequeue()
        print(node.data)
        if node.lchild:
            queue.enqueue(node.lchild)
        if node.rchild:
            queue.enqueue(node.rchild)


root=BST()
li=[70,40,20,80,90,100]
for i in li:
    insert_node(root,i)
level_order_traversal(root)


