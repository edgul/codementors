
class Dog:
    def __init__(self):
        self.name = "doggy"
        self._name = "_doggy"
        self.__name = "__doggy"
    def bark(self):
        """Makes the dog bark"""
        print("The dog is barking")
    def staticBark():
        print("The generic dog is barking")

d = Dog()
d.bark()
Dog.staticBark()
print(dir(d))
print(d.__class__)
print(d.__dict__)

print(help(Dog))
