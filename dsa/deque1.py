from collections import deque
dq=deque()
dq.append(10)
dq.appendleft(20)
dq.append(30)
print("Deque:",list(dq))
print("removed from front:",dq.popleft())
print("Removed from rear:",dq.pop())
