class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link =link
class linkedList:
    def __init__(self,head=None):
        self.head =head
    def insert_at_first(self,element):
        node=Node(element)
        if self.head is None:
            self.head=node
        else:
            node.link = self.head
            self.head=node
    def print(self):
        if self.head is None:
            print("linked list is  empty")
        ptr=self.head
        while(ptr!=None):
            print(ptr.data,end='-->')
            ptr=ptr.link
    def delete_last(self):
        ptr=self.head
        prev=ptr
        while(ptr.link!=None):
            prev=ptr
            ptr=ptr.link
        prev.link=None
    def delete_front(self):
        if self.head is None:
            print("linked list is empty")
        else:
            self.head=self.head.link
    def insert_at_position(self,element,position):
        node=Node(element)
        if self.head is None:
            self.head=node
        else:
            ptr=self.head
            count=1
            while(count!=position):
                ptr=ptr.link
                count+=1
            node.link=ptr.link
            ptr.link=node
    def delete_at_position(self,position):
        ptr=self.head
        count=1
        while(count!=position):
            count+=1
            prev=ptr
            ptr=ptr.link
        prev.link=prev.link.link



linked=linkedList()
linked.insert_at_first(10)
linked.insert_at_first(20)
linked.insert_at_first(30)
linked.insert_at_position(40,3)
linked.delete_at_position(2)
linked.print()
# linked.delete_last()
# print()
# linked.print()