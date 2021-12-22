# common stack operations:
# - Create stack
# - push
# - pop
# - peek
# - is Empty
# - is Full
# - Delete  stack

# Creation of stack
# 1.

class Stack:
    def __init__(self):
        self.stack =[]
    def __str__(self):
        self.stack=self.stack[::-1]
        val=[str(x) for x in self.stack]
        return '\n'.join(val)
    def isEmpty(self):
        if self.stack ==[]:
            return True
        else:
            return False
    def push(self,data):
        self.stack.append(data)
        print("element successfully pushed")
    def pop(self):
        if self.isEmpty():
            print("Nothing to pop")
        else:
            self.stack.pop()
            return 'element successfully popped'
    def peek(self):
        if self.isEmpty():
            return 'nothing in stack'
        else:
            print("top of stack is")
            print(f"stack is {self.stack}")
            return self.stack[0]
    def delete(self):
        if self.stack==[]:
            return 'already stack deleted'
        else:
            self.stack=[]

stack = Stack()
stack.isEmpty()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack)
print(stack.peek())
stack.delete()
print(f"stack=={stack}")