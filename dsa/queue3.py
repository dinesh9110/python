from queue import Queue
q=Queue()
q.put(10)
q.put(20)
q.put(30)
print("Front element:",q.queue[0])
print("Dequeued element:",q.get())
print("Queue size:",q.qsize())