class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Current balance:", self.balance)

acc = BankAccount("Greha", 1000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = int(input("Enter amount: "))
        acc.deposit(amt)

    elif choice == "2":
        amt = int(input("Enter amount: "))
        acc.withdraw(amt)

    elif choice == "3":
        acc.show_balance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
