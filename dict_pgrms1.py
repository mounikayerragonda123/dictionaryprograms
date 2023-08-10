#program to to find out number of occurrenecs of a character in a string
word=eval(input("enter string:"))
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
for k,v in d.items():
    print("{} occured  {} times".format(k,v))
    
#program to take dictionary from the keyboard and print sum of values
d=eval(input("enter dictionary:"))
s=sum(d.values())
print(s)

#program to number of vowels present in a string
word=eval(input("enter string:"))
vowels={'a','e','i','o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print("{} occured  {} times".format(k,v))
