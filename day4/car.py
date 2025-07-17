class pen:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def qual(self):
        print(f"pen name is {self.name} and pen price is {self.price}")
p=pen("XO",10)
p.qual()
