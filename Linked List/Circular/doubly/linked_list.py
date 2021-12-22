class Node:
    def __init__(self,data=None,nlink=None,plink=None):
        self.data=data
        self.nlink=nlink
        self.plink=plink

class Doubly_Circular_Linked_List:
    def __init__(self,head=None,tail=None):
        self.head=head
    def insert_start(self,data):
        node=Node(data)
        if self.head is None:
            node.nlink=node.plink=node
            self.head=node
            self.tail=node
        else:
            n=self.head
            while(n.nlink!=self.head):
                n=n.nlink
            node.nlink=self.head
            self.head.plink=self.head.nlink=node
            node.plink=self.head
            self.head=node
    def __iter__(self):
        n=self.head
        while(n):
            yield n
            if n.nlink==self.head:
                break
            n=n.nlink
    def print_reverse(self):
        n=self.tail
        while(n):
            # print(n.data)
            yield n
            if n.plink==self.tail:
                break
            n=n.plink
    def insert_at_end(self,data):
        node=Node(data)
        if self.head is None:
            node.nlink = node.plink = node
            self.head = node
            self.tail = node
        else:
            self.tail.nlink=node
            node.plink=self.tail
            node.nlink=self.head
            self.head.plink=node
            self.tail=node
    def delete_start(self):
        if self.head is None and self.tail is None:
            print("Nothingt to delete")
        else:
            self.head=self.head.nlink
            self.head.plink=self.tail
            self.tail.nlink=self.head
    def delete_end(self):
        if self.head is None and self.tail is None:
            print("Nothing to delete")
        else:
            self.tail=self.tail.plink
            self.tail.nlink=self.head
            self.head.plink=self.tail

dc=Doubly_Circular_Linked_List()
dc.insert_start(1)
dc.insert_start(2)
dc.insert_at_end(3)
dc.insert_at_end(4)
dc.delete_start()
dc.delete_end()
print(f"linked list are")
print([i.data for i in dc])
print("reverse printing")
print([i.data for i in dc.print_reverse()])
