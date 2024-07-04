class BankAccount:
    def __init__(self, accountName, accountNumber, accountBalance):
        self.accountName = accountName
        self.accountNumber = accountNumber
        self.accountBalance = accountBalance
    def Bank_Account(self):
        print(f' Account holder {self.accountName}, with account number {self.accountNumber}, having a closing balance of {self.accountBalance}')
        
    def Deposit(self):
        Deposit = 5000
        self.deposit = Deposit + self.accountBalance
        return self.deposit

    def Withdraw(self):
        Withdraw = 3000
        self.withdraw = self.deposit - Withdraw 
        return self.withdraw

    def CheckBalance(self):
        balance=self.withdraw
        return balance

account1=BankAccount('Abduljabbar', 1122334455, 10000)
account2=BankAccount('Salim', 6677889910, 5000)
print(f'first account balance will be: {BankAccount.Deposit(account1)}')
print(f'second account balance will be: {BankAccount.Withdraw(account1)}')
print(f'current account balance will be: {BankAccount.CheckBalance(account1)}')




class Person:
    def __init__(self, name, race, colour):
        self.name = name
        self.race = race
        self.colour = colour
    def Self_Person(self):
        print(f'This is {self.name}, {self.race} by race, skin colour is {self.colour}')

class Student(Person):
    def student(self, country):
        self.country = country
        print(f' Student name is {self.name}, {self.race} by race, skin colour is {self.colour} and from {self.country}')

class Lecturer(Person):
    def lecturer(self, tribe):
        self.tribe = tribe
        print(f' lecturer name is {self.name}, {self.race} by race, skin colour is {self.colour} and an {self.tribe} tribe')

person1= Person('Abduljabbar', 'African', 'dark')
person2= Student('Salim', 'Asian', 'brown')
person3= Lecturer('Dr. Humphery', 'American', 'white')
person1.Self_Person()
person2.student('China')
person3.lecturer('Indigeneous')