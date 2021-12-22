class Tree:
    def __init__(self,data,left=None,right=None):
        self.data =data
        self.left = left
        self.right=right
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if self.queue==[]:
            return 0
        else:
            return self.queue.pop(0)
    def __iter__(self):
        for i in self.queue:
            yield i
def post_order(rootnode):
    if not rootnode:
        return
    post_order(rootnode.left)
    post_order(rootnode.right)
    print(rootnode.data,end=' ')
def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.left)
    print(rootnode.data,end=' ')
    inorder(rootnode.right)
def level_order(rootnode):
    if rootnode is None:
        print("Tree empty")
    queue=Queue()
    queue.enqueue(rootnode)
    while list(queue)!=[]:
        popped_node=queue.dequeue()
        print(popped_node.data)
        if popped_node.left is not None:
            queue.enqueue(popped_node.left)
        if popped_node.right is not None:
            queue.enqueue(popped_node.right)
root=Tree(1)
l1=Tree(2)
l2=Tree(5)
root.left=l1
root.right=l2
l3=Tree(3)
l4=Tree(4)
l1.left=l3
l1.right=l4
post_order(root)
print("Level order traversal is ")
level_order(root)
