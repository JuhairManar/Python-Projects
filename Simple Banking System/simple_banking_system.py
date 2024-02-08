AC = {}

class Account:
    accId = 10001

    def __init__(self, name, age, nid_num, balance, password) -> None:
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance
        self.password = password
        self.account_id = Account.accId
        Account.accId += 1

    def check_balance(self, id):
        print("Your current balance is:", AC[id].balance)
        print('\n\n')

    def deposit(self, id, amount):
        AC[id].balance += amount
        print("Deposit successful. Current balance:", AC[id].balance)

    def withdraw(self, id, amount):
        if amount > AC[id].balance:
            print("Not enough balance to withdraw")
        else:
            AC[id].balance -= amount
            print("Withdrawal successful. Current balance:", AC[id].balance)

# Main menu loop
while True:
    print("Sir, How can we help you??? ")
    print("1. Open a new account")
    print("2. Check Balance")
    print("3. Deposit money")
    print("4. Withdraw Money")
    print("5. Show all bank accounts")
    op = int(input())
    print('\n\n')

    if op == 1:
        print("Sir, please provide the following information")
        name = input("Your name: ")
        age = int(input("Your age: "))
        nid = int(input("Your NID number: "))
        password = input("Enter a password: ")
        balance = int(input("Initial deposit amount:"))
        acc = Account(name, age, nid, balance, password)
        AC[acc.account_id] = acc
        print("Your account has been successfully created. Account ID:", acc.account_id, '\n\n')

    elif op == 2 or op == 3 or op == 4:
        x = int(input("Enter your account id: "))
        if x in AC:
            password = input("Enter your password: ")
            if AC[x].password == password:
                if op == 2:
                    AC[x].check_balance(x)
                elif op == 3:
                    amount = int(input("Enter the amount to deposit: "))
                    AC[x].deposit(x, amount)
                elif op == 4:
                    amount = int(input("Enter the amount to withdraw: "))
                    AC[x].withdraw(x, amount)
            else:
                print("Invalid password\n\n")
        else:
            print("Invalid account ID\n\n")

    elif op == 5:
        print("All bank accounts:")
        for id, acc in AC.items():
            print(f"Account ID: {id}, Name: {acc.name}, Balance: {acc.balance}")
        print('\n\n')

    else:
        print("Invalid choice. Please select a valid option.\n\n")
