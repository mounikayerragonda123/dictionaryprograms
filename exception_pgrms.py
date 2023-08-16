import sys
randomlist=['a',0,2]
for entry in randomlist:
    try:
        print("the entry is",entry)
        r=1/int(entry)
        break
    except:
        print("oops!",sys.exc_info()[0],"occured.")
        print("next entry")
        print()
print("The reciprocal of",entry,"is",r)

#program to print the reciprocal of even numbers
try:
    num=int(input("enter a number:"))
    assert num%2==0
except:
    print("Not an even number")
else:
    reciprocal=1/num
    print(reciprocal)
finally:
    print("Always executed")
    
#User defined Exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass
class ValueToosmallError(Error):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass
number=20
while True:
    try:
        i_num=int(input("enter a number"))
        if i_num<number:
            raise ValueToosmallError
        elif i_num>number:
            raise ValueTooLargeError
        break
    except ValueToosmallError:
        print("This value is too small,try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large,try again!")
        print()
print("Congratulations!You guessed it correctly.")
    