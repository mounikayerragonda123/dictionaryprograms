#polymorphism
class Parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrrot can't swim")
class penguin:
    def fly(self):
        print("penguin can't fly")
    def swim(self):
        print("penguin can swim")

def  flying_test(bird):
    bird.fly
blu=Parrot()
peggy=penguin()
flying_test(blu)
flying_test(peggy)