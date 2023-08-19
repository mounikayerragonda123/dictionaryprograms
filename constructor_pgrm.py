#constructors in python
class Employee:
    def __init__(self,eid,ename,ecity):#constructor 
        self.eid=eid
        self.ename=ename
        self.ecity=ecity
    def m1(self):
        print(self.eid,self.ename,self.ecity)
e=Employee(100,'mouni','bnglr')
e.m1()