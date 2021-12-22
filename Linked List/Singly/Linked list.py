class Node:
    def __init__(self,data=None,link=None):
        self.data = data
        self.link = link
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    def print(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n=self.head
            while(n != None):
                print(f"{n.data}-->",end='')
                n=n.link
    def print_in_List_Form(self):
        l=[]
        if self.head is None:
            print('Empty list')
        else:
            n=self.head
            while(n!=None):
                l.append(n.data)
                n=n.link
        return l
    def insert_at_begin(self,element):
        node = Node(element)
        if self.head is None:
            self.head = node
        else:
            node.link=self.head
            self.head=node
    def insert_at_end(self,element):
        node = Node(element)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while(n.link !=None):
                n=n.link
            n.link=node
    def insert_at_position(self,element,position):
        node=Node(element)
        if self.head is None:
            print("we cannot insert an element in particular posititon")
        else:
            pos=1
            n=self.head
            while(pos!=position):
                n=n.link
                pos+=1
            node.link = n.link
            n.link = node

    def delete_begin(self):
        if self.head is None:
            print("Deletion not possible")
        else:
            self.head=self.head.link
    def delete_end(self):
        if self.head is None:
            print("Deletion not possible")
        else:
            n=self.head
            prev=n
            while n.link!=None:
                prev=n
                n=n.link
            prev.link=None
    def delete_at_any_position(self,position):
        if self.head is None:
            print("Deletion not possible")
        else:
            pos=1
            n=self.head
            while(pos!=position):
                pos+=1
                n=n.link
            n.link=n.link.link
    def delete_by_value(self,value):
        if self.head is None:
            print("Deletion not possible")
        else:
            n=self.head
            c=0
            prev=n
            while(n!=None):
                if n.data==value:
                    c=c+1
                    break
                else:
                    prev=n
                    n=n.link
                    c+=1
            if c==1:
                self.head=self.head.link
            elif c>1:
                prev.link=prev.link.link
            else:
                print("value not present in Linked List")
    def __iter__(self):
        n=self.head
        while(n!=None):
            yield n
            n=n.link

linked_list=LinkedList()
linked_list.insert_at_begin(2)
linked_list.insert_at_begin(4)
linked_list.insert_at_end(6)
linked_list.insert_at_position(3,2)
linked_list.insert_at_position(7,1)
linked_list.insert_at_begin(1)
linked_list.insert_at_end(9)
linked_list.print()
print()
linked_list.delete_end()
linked_list.print()
print()
linked_list.delete_begin()
linked_list.print()
print()
linked_list.delete_at_any_position(3)
linked_list.print()
print()
linked_list.delete_by_value(6)
linked_list.print()
print()
print([i.data for i in linked_list])
# print(linked_list.print_in_List_Form())
