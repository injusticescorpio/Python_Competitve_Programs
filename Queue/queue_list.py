class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):#O(N**2) worst case
        self.queue.append(data)
        print("inserted element in queue")
    def __iter__(self):
        for i in self.queue:
            yield i
    def isEmpty(self):
        if self.queue==[]:
            return True
        else:
            return False
    def dequeue(self):
        if self.isEmpty():
            return "Nothing to delete"
        else:
            print(f"poped item=={self.queue[0]}")
            self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Nothing to peek"
        else:
            return self.queue[0]
    def delete_full_queue(self):#O(1) AND O(1) FOR TIME AND SPACE COMPLEXITY
        print("deleting full queue")
        self.queue=[]


queue = Queue()
print(queue.isEmpty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print([i for i in queue])
print(f"peek is {queue.peek()}")
queue.dequeue()
queue.dequeue()
print([i for i in queue])
print(f"peek is {queue.peek()}")
queue.delete_full_queue()
print(f"peek is {queue.peek()}")
