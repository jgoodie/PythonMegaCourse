#!/usr/local/bin/python3

# Base class
class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = float(file.read())

    def withdrawl(self, amount):
        self.balance = self.balance - amount
        
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
        
        
        
# Subclass
class Checking(Account):
    def __init__(self, filepath, fee): 
        self.fee = fee
        Account.__init__(self, filepath)       

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

        
# account = Account("balance.txt")
 
# print(account.balance) 
# account.withdrawl(100)
# print(account.balance)  
# account.deposit(500) 
# print(account.balance)
# account.commit()

checking = Checking("balance.txt", 1)
print(checking.balance) 
checking.deposit(110)
checking.commit()
print(checking.balance) 
checking.transfer(110)
print(checking.balance)
checking.commit()
  
            
