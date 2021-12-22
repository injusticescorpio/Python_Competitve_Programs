class Node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link
class Linked:
    def __init__(self,head=None):
        self.head=head
class Stack(Linked):
    def __init__(self):
        super().__init__()#we can also do like self.linked=Linked() and inorder access head we can do self.linked.head
    def isEmpty(self):#------------ time and space O(1)
        if self.head is None:
            return True
        else:
            return False
    def push(self,data):
        node=Node(data)
        if self.isEmpty():
            self.head=node
        else:
            node.link=self.head
            self.head=node
    def pop(self):
        if self.isEmpty():
            return "Nothing to pop"
        else:
            data=self.head.data
            self.head=self.head.link
            return data
    def __iter__(self):
        if self.head is None:
            print("stack empty")
        n=self.head
        while(n!=None):
            yield n
            n=n.link
    def del_stack(self):
        self.head=None
    def peek(self):
        if self.isEmpty():
            return "stack empty"
        else:
            return self.head.data


stack=Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
# stack.del_stack()
for i in stack:
    print('\t\t'+str(i.data))
    print("|_______________|")