class TwoStacks:
    def __init__(self,n):
        self.arr=[None]
        self.top1=-1
        self.top2=n
    def push1(self,item):
        if self.top1<self.top2-1:
            self.top2-=1
            self.arr[self.top2]=item
        else:
            print("stack overflow")
    def pop1(self):
        if self.top1>=0:
            item=self.arr[self.top1]
            self.top1-=1
            return item
        return "Stack underflow"
    def pop2(self):
        if self.top2 <len(self.arr):
            item=self.arr[self.top2]
            self.top2+=1
            return item
        return "stack underflow"
ts=TwoStacks(5)
ts.push1(10)
print(ts.pop1())
print(ts.pop2())
