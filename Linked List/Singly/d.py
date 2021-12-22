class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link
def insert_start(data,head):
    node = Node(data)
    if head is None:
        head=node
    else:
        node.link=head
        head=node
    return head
def sorted_list(a,res):
    if res==None or res.data>=a.data:
        res=insert_start(a.data,res)
        print(f"\na.data1={a.data} and res.data1=={res.data}")
    else:
        q=res
        node=Node(a.data)
        print('printing q')
        while(q!=None and node.data>q.data):
            print(f"node={node.data} and q=={q.data}")
            prev=q
            q=q.link
        if q == None:
            prev.link=node
        else:
            node.link=prev.link
            prev.link=node
    return res


lis=None
lis=insert_start(20, lis)
lis=insert_start(1,lis)
lis=insert_start(4,lis)
lis=insert_start(3,lis)

res=None
li=lis
print("Before sorting")
while(lis!=None):
    print(f"{lis.data}-->",end='')
    lis=lis.link
while(li !=None):
    res=sorted_list(li,res)
    li=li.link
print("\nAfter sorting")
while(res!=None):
    print(f"{res.data}-->",end='')
    res=res.link
