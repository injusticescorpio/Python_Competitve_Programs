class Node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link

def insert_end(data,head):
    node=Node(data)
    if head is None:
        head=node
    else:
        n=head
        while(n!=None):
            prev=n
            n=n.link
        prev.link=node
    return head

def reverse(data,prev):
    node=Node(data)
    node.link=prev
    prev=node
    return prev


b=insert_end(1,None)
b=insert_end(2,b)
b=insert_end(3,b)
ptr=ptr1=b
print("linked list is :)")
while(ptr!=None):
    print(f"{ptr.data}-->",end='')
    ptr=ptr.link
print()
prev=None
while(ptr1!=None):
    prev=reverse(ptr1.data,prev)
    ptr1=ptr1.link
print("Linked list in reverse form")
while(prev!=None):
    print(f"{prev.data}-->",end='')
    prev=prev.link