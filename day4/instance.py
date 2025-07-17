class Employee:
    company="TechCorp"
    def __init__(self,name):
        self.name=name
e1=Employee("Alice")
e2=Employee("Bob")
print(e1.name,e1.company)
print(e2.name,e2.company)