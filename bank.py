import re


class Bank:
    def __init__(self):
        self.accounts = {}
        self.last_account_number = 0

    def add_accounts(self, name):
        self.last_account_number += 1
        account = Account(name, self.last_account_number)
        self.accounts[self.last_account_number] = account


class Account:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self._password = 0
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        valid_pass = re.match(r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$", password)
        if valid_pass:
            self._password = password
        else:
            print("Minimum eight characters, at least one upper letter and one number")

    def show_info(self):
        print(f"Name: {self.name}, Account number: {self.account_number}, Balance: {self.balance}")

    def deposit(self, value, password):
        if password == self.password:
            self.balance += value
        else:
            print("incorrect password!")

    def withdraw(self, value, password):
        if password == self.password:
            self.balance -= value
        else:
            print("incorrect password!")

bank = Bank()
bank.add_accounts("farhad")
bank.add_accounts("ali")
farhad = bank.accounts[1]
farhad.password = "Farhad78"
print(farhad.password)
farhad.deposit(20000, "Farhad78")
farhad.withdraw(5000, "Farhad78")
farhad.show_info()