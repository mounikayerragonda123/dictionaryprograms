#pickling and unpickling programs
import pickle
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno,'\t',self.ename,'\t',self.esal)
with open("emp.data","wb") as f:
    e=Employee(100,'mouni',1000000)
    pickle.dump(e,f)
    print("pickling of employee object completed")
with open("emp.data","rb") as f:
    e=Employee(100,'mouni',1000000)
    obj=pickle.load(f)
    print("employee information after pickling")
    obj.display()
        