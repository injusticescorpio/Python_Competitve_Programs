class Heap:
    def __init__(self,size):#Time:O(1) space O(n)
        self.li=[None]*(size+1)#not using zeroth index
        self.last_used_index=0
        self.maxsize=size+1
def peek(root):#time and space is O(1)
    if not root:
        return
    else:
        return root.li[1]
def size(root):#time and space is O(1)
    if not root:
        return
    return root.last_used_index
def level_order_traversal(root):#Time is O(n) and space is O(1)
    if not root:
        return
    for i in range(1,root.last_used_index+1):
        print(root.li[i])
def heapifyTreeinsert(root,index,heaptype):#Time complexity is O(logn+logn+1+1+1...++1)==o(logn) and space is O(logn)
    # print(f"index=={index}")
    parent_index=index//2
    if index<=1:
        return
    #MINIMUM Heap
    if heaptype=='Min':
        if root.li[index]<root.li[parent_index]:
            root.li[index],root.li[parent_index]=root.li[parent_index],root.li[index]
        heapifyTreeinsert(root,parent_index,heaptype)
    #Max heap
    elif heaptype=='Max':
        if root.li[index]>root.li[parent_index]:
            root.li[index],root.li[parent_index]=root.li[parent_index],root.li[index]
        heapifyTreeinsert(root,parent_index,heaptype)

def insert_node(root,data,heaptype):
    if root.last_used_index+1==root.maxsize:
        return 'Heap is full'
    root.li[root.last_used_index+1]=data
    root.last_used_index+=1
    heapifyTreeinsert(root,root.last_used_index,heaptype)
    return 'value inserted'
def heapifyTreeExtract(root,index,heaptype):
    leftindex=2*index
    rightindex=2*index+1
    swap_child=0

    if root.last_used_index<leftindex:
        return
    elif root.last_used_index==leftindex:#one child condition
        if heaptype=='Min':
            if root.li[index]>root.li[leftindex]:
                root.li[index],root.li[leftindex]=root.li[leftindex],root.li[index]
                return
        else:
            if root.li[index] < root.li[leftindex]:
                root.li[index], root.li[leftindex] = root.li[leftindex], root.li[index]
                return
    else:#two child condition
        if heaptype=='Min':
            if root.li[leftindex]<root.li[rightindex]:
                swap_child=leftindex
            else:
                swap_child=rightindex
            if root.li[index]>root.li[swap_child]:
                root.li[index], root.li[swap_child] = root.li[index], root.li[swap_child]
        else:
            if root.li[leftindex]>root.li[rightindex]:
                swap_child=leftindex
            else:
                swap_child=rightindex
            if root.li[index]<root.li[swap_child]:
                root.li[index], root.li[swap_child] = root.li[index], root.li[swap_child]
        heapifyTreeinsert(root,swap_child,heaptype)

def extractNode(root,heaptype):
    if root.last_used_index==0:
        return
    else:
        extractNode=root.li[1]
        root.li[1]=root.li[root.last_used_index]
        root.li[root.last_used_index]=None
        root.last_used_index-=1
        heapifyTreeExtract(root,1,heaptype)
        return extractNode
def delete_entire_tree(root):
    root.li=[None]*root.maxsize
    root.last_used_index=0

root=Heap(10)
insert_node(root,4,'Max')#last_used_index=0
insert_node(root,5,'Max')#last_used_index=1
insert_node(root,2,'Max')
insert_node(root,1,'Max')
# insert_node(root,15,'Max')
print(f"level_order_traversal")
level_order_traversal(root)
print(f"extracted node is")
print(extractNode(root,'Max'))
print(f"level_order_traversal")
level_order_traversal(root)
delete_entire_tree(root)

insert_node(root,1,'Max')
print(f"level_order_traversal")
level_order_traversal(root)