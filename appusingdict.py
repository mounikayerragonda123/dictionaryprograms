#program  to create a dictionary using student and marks and access the marks by using student name
n=int(input("enter number of students:"))
d={}
print("hello")
for i in range(n):
    name=input("enter student name:")
    marks=int(input("enter student marks:"))
    d[name]=marks
print(d)
while True:
    name=input("enter student name to get marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("student not found")
    else:
        print("the marks of {}:{}".format(name,marks))
    option=input("Do you want to find another student marks [Yes/No]:")
    if option=="No":
        break
print("thanks for using our application")