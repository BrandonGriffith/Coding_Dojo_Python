class BankAccount:

    accounts = []

    def __init__(self,int_rate,balance,account):
        self.int_rate = int_rate
        self.balance = balance
        self.type = account
        BankAccount.accounts.append(self)

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

    def deposit(self, amount):
        self.balance += amount
        print(f"Your account value is now ${self.balance}")
        return self

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Your account value is now ${self.balance}")
        else:
            print(f"Your account value is: ${self.balance} in your {self.type} account. You can not withdraw ${amount}")
            print("Insufficient Funds fee: Charging your account $5")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Your {self.type} account balance is: ${self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            x = self.balance
            self.balance += (self.balance * self.int_rate)
            x = self.balance - x
            print(f"Your {self.type} account has incressed by ${x} because of interest")
        else:
            print("No money no interest")
        return self

savings = BankAccount(.04,0,"Savings")
checking = BankAccount(.02,0,"Checking")
print("--------------------------------------------------------------------------------------------------")
savings.deposit(100).deposit(200).deposit(300).withdraw(400).yeild_interest().display_account_info()
print("--------------------------------------------------------------------------------------------------")
checking.deposit(100).deposit(200).withdraw(100).withdraw(50).withdraw(45).withdraw(300).yeild_interest().display_account_info()
print("--------------------------------------------------------------------------------------------------")

BankAccount.print_all_accounts()
