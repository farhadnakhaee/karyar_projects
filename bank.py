import re
from datetime import datetime


def write_file(f):
    """Decorator for writing operation."""
    def wrapper(self, *args):
        f(self, *args)
        self.file.write(f"Func: {f.__name__}, Balance: {self.balance}, at {datetime.now()}\n")
    return wrapper


class Bank:
    def __init__(self):
        self.accounts = {}
        self.last_account_number = 0

    @staticmethod
    def _input_menu_number():
        return input("Hello!\n\n1. Login\n2. sign up\n3. Exit\n\nEnter a number (1, 2, 3): ")

    def add_account(self, name):
        self.last_account_number += 1
        account = Account(name, self.last_account_number)
        self.accounts[self.last_account_number] = account

    def satna(self, src_acc_num, dest_acc_num, value):
        try:
            dest_acc = self.accounts[dest_acc_num]
            src_acc = self.accounts[src_acc_num]
        except KeyError:
            print("id is incorrect")
        else:
            if src_acc.balance > value:
                src_acc.withdraw(value)
                dest_acc.deposit(value)
            else:
                print("value is low.")

    def run(self):
        while True:
            menu_number = self._input_menu_number()
            if menu_number == "1":
                account_number = int(input('enter your account number: '))
                self._login(account_number)
            elif menu_number == '2':
                name = input('whats your name? ')
                self._sign_up(name)
            else:
                break

    def _sign_up(self, name):
        self.add_account(name)
        print(f"\nsign up is complete for '{name}'!")
        print(f"your account number: {self.last_account_number}")
        print(f"your password: {self.accounts[self.last_account_number].password}")
        print('please login!\n')

    def _login(self, account_number):
        if account_number in self.accounts.keys():
            password = input('Enter your password: ')
            if password == self.accounts[account_number].password:
                self._operation_if_access(account_number)
            else:
                print('password is incorrect.')
        else:
            print('username is not available.')

    def _operation_if_access(self, account_number):
        account = self.accounts[account_number]
        while True:
            print('\nWelcome to Bank!')
            print('1. show info\n2. deposit\n3. withdraw\n4. satna\n5. set password\n6. Exit')
            select_option = input('\nEnter menu number: ')
            if select_option == '1':
                account.show_info()
            elif select_option == '2':
                value = int(input('enter value: '))
                account.deposit(value)
            elif select_option == '3':
                value = int(input('enter value: '))
                account.withdraw(value)
            elif select_option == '4':
                value = int(input('enter value: '))
                dest_account_number = int(input('enter destination account number: '))
                self.satna(account_number, dest_account_number, value)
            elif select_option == '5':
                password = input('enter a password:\n(Minimum eight characters, at least one upper letter and one number)')
                account.password = password
            else:
                break


class Account:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self._password = "1111"
        self.file = File(account_number)

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

    @write_file
    def show_info(self):
        print(f"Name: {self.name}, Account number: {self.account_number}, Balance: {self.balance}")

    @write_file
    def deposit(self, value):
        self.balance += value

    @write_file
    def withdraw(self, value):
        self.balance -= value


class File:
    def __init__(self, account_number):
        self.account_number = account_number
        with open(f"{account_number}.txt", "w") as f:
            f.write(f"History for {account_number}:\n")

    def write(self, data):
        with open(f"{self.account_number}.txt", "a") as f:
            f.write(data)

    def read(self):
        with open(f"{self.account_number}.txt", "r") as f:
            return f.read()


if __name__ == "__main__":
    bank = Bank()
    bank.run()
