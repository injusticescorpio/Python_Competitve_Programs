class Node:
    def __init__(self,data=None,link=None):
        self.data = data
        self.link =link

class Circular_Linked:
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail
    def __iter__(self):
        n=self.head

        while(n):
            yield n
            if n.link==self.head:
                break
            n=n.link
    #Time and space complexity is O(1)
    def create_circular_list(self,data):
        node=Node(data=data)#>>>>>>>>>>>>>>>>>>>>>>>O(1)
        node.link=node#>>>>>>>>>>>>>>>>>>>>>>>>>>>>O(1)
        self.head=node                              #O(1)
        self.tail=node
        return "The circular linked list have been created"
    def insert_start(self,data):
        node=Node(data)
        if self.head is None:
            node.link=node
            self.head=node
            self.tail=node
        else:
            n=self.head
            while(n.link!=self.head):
                n=n.link
            node.link=self.head
            self.head=node
            n.link=self.head
    def insert_end(self,data):
        node = Node(data)
        if self.head is None:
            node.link = node
            self.head = node
            self.tail = node
        else:
            self.tail.link=node
            self.tail=node
            self.tail.link=self.head
    def insert_at_position(self,data,position):
        node=Node(data)
        if self.head is None:
            print("insertion not possible")
        else:
            pos=1
            n=self.head
            while(pos!=position):
                prev=n
                n=n.link
                pos+=1
            node.link=prev.link
            prev.link=node
    def delete_start(self):
        if self.head is None:
            print("deletion not possible")
        else:
            n=self.head
            while(n.link!=self.head):
                n=n.link
            self.head=self.head.link
            n.link=self.head
    def delete_end(self):
        if self.head is None:
            print("deletion not possible")
        else:
            n=self.head
            prev=None
            while(n.link!=self.head):
                prev=n
                n=n.link
            #deleting first node
            if prev is None:
                self.head =prev
            else:
                prev.link=self.head
                self.tail=prev
    def delete_at_position(self,position):
        if self.head is None:
            print("deletion not possible")
        else:
            pos=1
            n=self.head
            while(pos!=position):
                prev=n
                pos+=1
                n=n.link
            prev.link=prev.link.link
            
            

circular=Circular_Linked()
circular.insert_start(1)
circular.insert_start(2)
circular.insert_start(3)
circular.insert_end(4)
circular.insert_end(5)
circular.insert_at_position(10,2)
circular.insert_at_position(20,3)
circular.delete_start()
circular.insert_start(100)
circular.delete_end()
circular.delete_at_position(4)
circular.delete_start()
print([i.data for i in circular])