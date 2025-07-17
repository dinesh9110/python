class CircularQueue:
    def __init__(self,size):
        self.queue=[None]*size
        self.max_size=size
        self.front=self.rear=-1
    def enqueue(self,item):
        if(self.rear+1)%self.max_size==self.front:
            print("Queue is full")
            return
        elif self.front==-1:
            self.front=0
        self.rear=(self.rear+1)%self.max_size
        self.queue[self.rear]=item
    def dequeue(self):
        if self.front==-1:
            print("Queue is empty")
            return
        removed =self.queue[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.max_size
        return removed
cq=CircularQueue()
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.dequeue()
cq.enqueue(40)
print(cq.queue())