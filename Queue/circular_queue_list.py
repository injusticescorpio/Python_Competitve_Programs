class Circular_queue:
    def __init__(self,size):
        self.queue=[None]*size#->>space complexity O(n) rest all in function O(1)
        self.size=size
        self.top=-1
        self.start=0
    def __str__(self):
        values=[str(i) for i in self.queue]
        return ' '.join(values)
    def isFull(self):#________O(1)time O(1) space complexity
        if self.top+1==self.start and self.start==0 and self.top+1==self.size :
            return True
        else:
            return False
    def isEmpty(self):#--------------->O(1)
        if self.top==-1:
            return True
        else:
            return False
    def enqueue(self,data):#-------->O(1)
        if self.isFull():
            return "queue is Full"
        else:
            if self.top+1==self.size:
                self.top=0
            else:
                self.top+=1
            # if self.start==-1:
            #     self.start=0
            self.queue[self.top]=data
            print("element inserted")
    def dequeue(self):#---------->time complexity O(1) and space complexity O(1)
        if self.isEmpty():
            print("queue is empty")
        else:
            first_element=self.queue[self.start]
            # print(f'first_element=={first_element}')
            if self.start==self.top:
                self.queue[self.start]=None
                self.start=self.top=-1
            elif self.start+1==self.size:
                self.start=0
                print(f"self.start={self.start}")
            else:
                self.queue[self.start]=None
                self.start+=1
                print(f"popped item is {first_element}")
    def peek(self):#-------->O(1) time and O(1) space
        if self.isEmpty():
            print("queue is empty")
        else:
            return self.queue[self.start]
    def delete(self):#------>O(1) time and O(1) space
        self.queue=[None]*self.size
        self.top=-1
        self.start=0
        


queue = Circular_queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue)
# queue.dequeue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
# queue.dequeue()
queue.enqueue(1)
print(queue)