class Dog:
    def __init__(self,breed):
        self.breed=breed
    def bark(self):
        print(f"{self.breed} says woof !")
d=Dog("Beagle")
d.bark()
