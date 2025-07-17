from queue import Queue
class StackUsingQueue:
    def __init__(self):
        self.q=Queue()
    def push(self,item):
        size=self.q.qsize()
        self.q.put(item)
        for _ in range(size):
            self.q.put(self.q.get())
    def pop(self):
        if self.q.empty():
            return "stack is empty"
        return self.q.get()
stack=StackUsingQueue()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.pop())
print(stack.pop())