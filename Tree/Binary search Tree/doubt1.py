class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert1(self,root,val):
        if val<=root.info:
            if root.left is not None:
                root.left=self.insert1(root.left,val)
            else:
                root.left=Node(val)
                return root
        else:
            if root.right is not None:
                root.right = self.insert1(root.right, val)
            else:
                root.right = Node(val)
                return root


    def insert(self,val):
        if self.root is None:
            self.root =Node(val)
            return
        else:
            print("exe")
            self.insert1(self.root,val)







tree= BinarySearchTree()

t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)