dict={} # creation of empty dictionary
print(type(dict))
d={1:'mounika',2:'lakshmi',3:'pravalika'}
print(d[1]) # acessing elements  inside of the dictionary
print(d[3])
print(d.keys())
for i,k in d.items(): # accessing all the items in the string
    print(i,k)
for i in d.keys():
    print(i)
for i in d.values():# accessing values in a list
    print(i)
d1={'a':'apple','b':'ball','c':'cat'}
d.update(d1) #to add elements to dictionary from another dictionary
print(d)
