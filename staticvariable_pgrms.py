#various places to declare static variables
class Test:
    a=10
    def __init__(self):
        self.b=20
        self.c=30
    def n1(self):
        self.d=40
    @classmethod
    def m2(cls):
        cls.f=60
        cls.g=70
    @staticmethod
    def m3():
        Test.h=40
    
    
t=Test()
t.n1()
print(Test.__dict__)#gives all the static variables in a class 
print(t.a,t.b,t.c,t.d)
Test.m3()
Test.m2()
print(t.h,t.g,t.f)

        