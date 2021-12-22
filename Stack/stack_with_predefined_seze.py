class Stack:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.stack = []
    def __iter__(self):
        self.stack = self.stack[::-1]
        for i in self.stack:
            yield i
    def isEmpty(self):
        if self.stack ==[]:
            return True
        else:
            return False
    def is_Full(self):
        if len(self.stack)==self.maxsize:
            return True
        else:
            return False
    def push(self,data):
        if self.is_Full():
            print("max limit reached")
        else:
            self.stack.append(data)
    def pop(self):
        if self.isEmpty():
            print("nothing to pop")
        else:
            self.stack.pop()
    def peek(self):
        if self.isEmpty():
            print("nothing to pop")
        else:
            return self.stack[0]

    def delete(self):
        if self.isEmpty():
            print("already deleted")
        else:
            self.stack=[]
            print("deleted successfully")




stack=Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
print("stack is")
for i in stack:
    print('\t'+str(i))
    print("|----------|")
print(f"top of stack is {stack.peek()}")

