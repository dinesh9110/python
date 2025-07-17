class Person:
    def __init__(self,name,dept,age,status):
        self.name=name
        self.dept=dept
        self.age=age
        self.status=status
    def greet(self):
        print(f"hello,my name is {self.name},iam from {self.dept},iam {self.age} years old ,iam {self.status}")
p=Person("Dinesh","cse",18,"single")
p.greet()