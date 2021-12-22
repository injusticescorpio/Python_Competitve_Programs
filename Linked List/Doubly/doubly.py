class Node:
    def __init__(self,data=None,nlink=None,plink=None):
        self.data = data
        self.nlink = nlink
        self.plink = plink
class Double_Linked_List:
    def __init__(self,head=None):
        self.head = head
    def insert_at_start(self,data):
        node=Node(data)
        if self.head is None:
            self.head = node
        else:
            node.nlink = self.head
            self.head.plink=node
            self.head=node
    def print(self):
        if self.head is None:
            print("Linked list is empty therefor forward traversal not possible")
        else:
            print("Linked List in Normal order")
            n=self.head
            while(n!=None):
                print(f"{n.data}-->",end='')
                n=n.nlink
    def print_reverse(self):
        if self.head is None:
            print("Linked list is empty therefore forward traversal not possible")
        else:
            print("\nLinked List in reverse order")
            n=self.head
            while(n!=None):
                prev=n
                n=n.nlink
            p=prev
            while(p!=None):
                print(f"{p.data}-->",end='')
                p=p.plink
            print()
    def insert_at_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while(n.nlink!=None):
                n=n.nlink
            node.plink=n
            n.nlink=node
    def insert_at_position(self,data,pos):
        if self.head is None:
            print("insertion not possible")
        else:
            print("\ninseting an element after position")
            node=Node(data)
            c=1
            n=self.head
            while(c!=pos):
                c+=1
                n=n.nlink
            node.nlink=n.nlink
            n.nlink.plink=node
            node.plink=n
            n.nlink=node
    def delete_at_start(self):
        if self.head is None:
            print("Deletion not possible")
        else:
            self.head=self.head.nlink
            self.head.plink=None
    def full_deletion(self):
        if self.head is None:
            print("Nothing to delete")
        else:
            self.head=None



d=Double_Linked_List()
d.insert_at_start(2)
d.insert_at_start(4)
d.insert_at_start(5)
d.insert_at_end(9)
d.print()
d.insert_at_position(10,3)
d.delete_at_start()
d.print()
d.print_reverse()
print("Deleting full linked list :)")
d.full_deletion()
d.print()
d.print_reverse()
