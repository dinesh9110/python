def reverse_queue(q):
    stack=[]
    while q:
        stack.append(q.pop(0))
    while stack:
        q.append(stack.pop())
queue=[10,20,30,40]
reverse_queue(queue)
print(queue)