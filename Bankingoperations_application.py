#Application to create perform operations on bank
import sys
class Customer:
    '''customer class with bank operations.'''
    bankname='sbi'
    def __init__(self,name,balance=0.001):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print('Balance after Deposit:',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('insufficient funds ..cannot perform operations')
            sys.exit()
        self.balance=self.balance-amt
        print('Balance after deposit:',self.balance)
    
print('Welcome to',Customer.bankname)
name=input("enter your name:")
c=Customer(name)
while True:
    print('d-deposit \n w-withdraw \n e-exit')
    option=input("choose your option:")
    if option=='d' or option=='D':
        amt=float(input('enter the amount:'))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input('enter the amount:'))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks for Banking")
        sys.exit()
    else:
        print("invalid option choose valid option")    