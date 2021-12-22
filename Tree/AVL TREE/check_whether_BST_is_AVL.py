class AVL:
    def __init__(self,data=None):
        self.data = data
        self.lchild=None
        self.rchild=None
        self.height=1
class BST:
    def __init__(self,data=None):
        self.data = data
        self.lchild=None
        self.rchild=None


class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
        return "Data inserted successfully"
    def dequeue(self):
        if self.queue==[]:
            return 'Nothing to pop'
    def __iter__(self):
        for i in self.queue:
            yield i


def insert_node_BST(root,data):
    if root.data is None:
        root.data=data
    elif data<=root.data:
        if root.lchild:
            insert_node_BST(root.lchild,data)
        else:
            root.lchild=BST(data)
    else:
        if root.rchild:
            insert_node_BST(root.rchild,data)
        else:
            root.rchild=BST(data)

def level_order_traversal(root):
    pass




root=BST()



