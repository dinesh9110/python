"""   
infix: An expression in which the operator is in between its two operands. A+B

prefix expression: An Expression in which operator preecedes its two operands is called an prefix expression.

post expression:



1.given a expression in the infix form
2.Find the highest precedence operator
3.if there are more then one operators
"""

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is empty"
    def is_empty(self):
       return len(self.stack)==0
    def size(self):
        return len(self.stack)
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("Top element:",s.peek())
print("popped element:",s.pop())
print("Stack Size:",s.size())
s.size()