#create Binary tree using linked list
class Tree:
    #creation of tree
    def __init__(self,data,leftchild=None,rightchild=None): #time and space complexity is O(1)
        self.data=data
        self.leftchild=leftchild
        self.rightchild=rightchild

def preorderTraversal(rootNode): #Time and space complexity is O(n)
    # print(f"root node =={rootNode}")
    if not rootNode:#----------------->O(1)
        # print(f"rootnode=={rootNode}")
        return
    print(rootNode.data)#O(1)
    preorderTraversal(rootNode.leftchild)#O(n/2)
    preorderTraversal(rootNode.rightchild)#O(n/2)
def inorderTraversal(rootNode): #Time and space complexity is O(N)
    if not rootNode:
        # print(f"rootnode=={rootNode}")
        return
    inorderTraversal(rootNode.leftchild)#O(N/2)
    print(rootNode.data)
    inorderTraversal(rootNode.rightchild)#O(n/2)
def postorderTraversal(rootNode):
    if not rootNode:
        return
    postorderTraversal(rootNode.leftchild)
    postorderTraversal(rootNode.rightchild)
    print(rootNode.data)


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

def levelorderTraversal(rootNode):
    if not rootNode:
        return
    queue=Queue()
    queue.enqueue(rootNode)
    while(list(queue)!=[]):
        root=queue.dequeue()
        print(root.data)
        if root.leftchild is not None:
            queue.enqueue(root.leftchild)
        if root.rightchild is not None:
            queue.enqueue(root.rightchild)
def searchBT(rootNode,nodeVal):
    if not rootNode:
        return 'BT does not exist'
    else:
        queue=Queue()
        queue.enqueue(rootNode)
        while (list(queue)!=[]):
            root=queue.dequeue()
            if root.data==nodeVal:
                return(f"node found at level")
            if root.leftchild:
                queue.enqueue(root.leftchild)
            if root.rightchild:
                queue.enqueue(root.rightchild)

        return 'Element not found'
def insertBT(rootnode,node):
    if not rootnode:
        rootnode =node
    else:
        queue=Queue()
        queue.enqueue(rootnode)
        while(list(queue)!=[]):
            root = queue.dequeue()
            if root.leftchild:
                queue.enqueue(root.leftchild)
            else:
                root.leftchild=node
                print("successfully inserted")
                return
            if root.rightchild:
                queue.enqueue(root.rightchild)
            else:
                root.rightchild=node
                print("successfully inserted")
                return
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        queue =Queue()
        queue.enqueue(rootNode)
        while(list(queue)!=[]):
            root=queue.dequeue()
            if root.leftchild:
                queue.enqueue(root.leftchild)
            if root.rightchild:
                queue.enqueue(root.rightchild)
        deepestNode=root
        return deepestNode

                
def delete_deepest_node(rootNode,deepestNode):
    if not rootNode:
        return
    queue =Queue()
    queue.enqueue(rootNode)
    while(list(queue)!=[]):
        root=queue.dequeue()
        if root==deepestNode:
            root=None
            return
        if root.leftchild:
            if root.leftchild==deepestNode:
                root.leftchild=None
                return
            else:
                queue.enqueue(root.leftchild)
        if root.rightchild:
            if root.rightchild==deepestNode:
                root.rightchild=None
                return
            else:
                queue.enqueue(root.rightchild)
def deleteBT(rootnode,data):
    if not rootnode:
        return "Binary tree doesnot exist"
    else:
        queue=Queue()
        queue.enqueue(rootnode)
        while(list(queue)!=[]):
            root=queue.dequeue()
            if root.data==data:
                print(f"successfully deleted {data} from tree")
                deppest_node=getDeepestNode(rootnode)
                delete_deepest_node(rootnode,deppest_node)
                root.data=deppest_node.data
                return
            if root.leftchild:
                queue.enqueue(root.leftchild)
            if root.rightchild:
                queue.enqueue(root.rightchild)
        print("Element not found")
def delete_entire(rootnode):
    if not rootnode:
        print("Already deleted")
    else:
        rootnode.data=rootnode.leftchild=rootnode.rightchild=None
        print("Deletion done")

BinaryTree=Tree("Drinks")
leftchild=Tree("Hot")
rightchild=Tree("Cold")
BinaryTree.leftchild=leftchild
BinaryTree.rightchild=rightchild
leftchild1=Tree("Tea")
leftchild2=Tree("Red label")
leftchild.leftchild=leftchild1
leftchild1.leftchild=leftchild2
print("Preorder traversal is:")
preorderTraversal(BinaryTree)
print("Inorder traversal is:")
inorderTraversal(BinaryTree)
print("Post order Traversal")
postorderTraversal(BinaryTree)
print("Level order Traversal")
levelorderTraversal(BinaryTree)
print(searchBT(BinaryTree,'Cold'))
##insertion
newnode=Tree("Ripple Tea")
insertBT(BinaryTree,newnode)


print("Level order Traversal")
levelorderTraversal(BinaryTree)
# deep_node=getDeepestNode(BinaryTree)
# print(f"deep_node=={deep_node}")
# delete_deepest_node(BinaryTree,deep_node)
# deleteBT(BinaryTree,'Cold1')
# delete_entire(BinaryTree)
print("Level order Traversal")
levelorderTraversal(BinaryTree)