class Animal:
    def makesound(self):
        print("Animal Sound")
class Dog(Animal):
    def makesound(self):
        print("Dog Sound")
class Cat(Animal):
    def makesound(self):
        print("Cat Sound")
class Tiger(Animal):
    def makesound(self):
        print("Tiger Sound")
    def hunting(self):
        print("Tiger Hunting")
def perform(ref):
    ref.makesound()
    if isinstance(ref,Tiger):
        ref.hunting()
perform(Dog())
perform(Cat())
perform(Tiger())