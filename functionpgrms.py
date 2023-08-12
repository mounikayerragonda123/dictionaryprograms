#intrduction of dictionaries
def add(a,b):
    '''This is function of 
            adding two numbers'''
    return a+b
print(add(20,30))
def display(**kwargs): # variable length argumnets
    for k,v in kwargs.items():
        print(k,"....",v)
display(name='durga',marks=100,age='24')

#anonymous function
s=lambda x:x*x
print(s(5))
l=[1,2,3,4,5,6]
l1=list(map(lambda x:x*x,l))
print(l1)
l2=list(filter(lambda x:x%2==0,l))
print(l2)

from functools import reduce
l=[1,2,3,4,5]
result=reduce(lambda x,y:x+y,l)
print(result)