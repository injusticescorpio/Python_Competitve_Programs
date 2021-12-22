class Tree:
    def __init__(self,data,lchild=None,rchild=None):
        self.data =data
        self.lchild = lchild
        self.rchild = rchild

def preorder(root):
    if not root:
        return
    print(root.data)
    preorder(root.lchild)
    preorder(root.rchild)

def main(root):
    comb=[]
    def dfs(root,val):
        if not root:
            return 0
        val+=root.data
        if not root.lchild and not root.lchild:
            comb.append(val)
            return val
        return dfs(root.lchild,val)+dfs(root.rchild,val)
    print(dfs(root,0))
    print(comb)




t=Tree(4)
l=Tree(1)
r=Tree(2)
t.lchild=l
t.rchild=r
print("preorder")
preorder(t)
main(t)