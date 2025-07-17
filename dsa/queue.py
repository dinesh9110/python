class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"
    def is_empty(self):
        return len(self.queue)==0
    def front(self):
        return self.queue[0] if not self.is_empty() else "Queue is empty"
    def size(self):
        return len(self.queue)
q=Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.enqueue("d")
print("Front element:",q.front())
print("Dequeued element:",q.dequeue())
print("queue size:",q.size())