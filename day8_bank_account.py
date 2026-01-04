class BankAccount:
     def __init__(self, holder, balance):
          self.holder = holder
          self.balance = balance
     def withdraw(self, amount):
          self.balance -= amount
     def deposit(self, amount):
          self.balance += amount
     def show_balance(self):
          print(self.holder, "balance:",self.balance)
acc = BankAccount("Greha", 100000)
acc.deposit(10000)
acc.withdraw(20000)
acc.show_balance()