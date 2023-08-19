#inheritance program
class car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def carname(self):
        print("the car owner is:",self.ename)
    def display(self):
        print(self.name,self.model,self.color)
class employee(car):
    def __init__(self,eid,ename,ecity):
        self.eid=eid
        self.ename=ename
        self.ecity=ecity
    def edisplay(self):
        print(self.eid,self.ename,self.ecity)# we getting the values from the parent class
c=employee('100','mouni','bnglr')
c.edisplay()
c.carname()
        