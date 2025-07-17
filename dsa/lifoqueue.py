from queue import LifoQueue
stack=LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40)
print("top element:",stack.queue[-1])
print("popped element:",stack.get())
print("Stack size:",stack.qsize())