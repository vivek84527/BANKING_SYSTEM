import sys


class customer:
    Bank_Name = 'State Bank Of India'

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print('your Bank balnce is:', self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('After deposit the amount your balance:', self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("sorry insufficient balance ..you can't process this transaction")
            sys.exit()
        self.balance = self.balance - amount
        print('your balance after withdraw:', self.balance)


print('Welcome to ', customer.Bank_Name)
name = input('Enter your name:-')
c = customer(name)
print("WELLCOME" + " " + name)

while True:
    print('--------------------------------------------------------')
    print('d-deposit\nw-withdraw\nc-Check Balance\ne-exit')
    option = input('Enter your choice:')

    if option == 'd' or option == 'D':
        amount = float(input('Enter the amount for deposit:'))
        c.deposit(amount)

    elif option == 'w' or option == 'W':
        amount = float(input('Enter the amount for withdraw:'))
        c.withdraw(amount)

    elif option == 'c' or option == 'C':
        c.check_balance()


    elif option == 'e' or option == 'E':
        print('Thanks for using State Bank of India')
        sys.exit()
    else:
        print('choose valid option')
