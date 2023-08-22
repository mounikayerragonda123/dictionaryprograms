#to check valid gmail id or not
import re
s=input("enter mail id")
m=re.fullmatch('\w[a-zA-Z0-9.]*@gmail[.]com',s)
if m!=None:
    print("valid mail id")
else:
    print("invalid mail id")
    
    
#to check valid registration number or not
import re
s=input('enter registration number:')
m=re.fullmatch('TS[012][0-9][A-Z]{2}\d{4}',s)
if m!=None:
    print("valid number")
else:
    print("invalid main id")