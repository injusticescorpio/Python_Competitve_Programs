class Node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link
class Linked_List:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
class Queue(Linked_List):# inheritance child of linked list
    def __init__(self):
        super().__init__()

    def enqueue(self,data):
        node=Node(data)


queue=Queue()