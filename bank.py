import re


def check_pass(f):
    """
    decoratore for check password.
    """
    def wrapped(self, password, *args):
        if password == self.password:
            f(self, password, *args)
        else:
            print("password is incorrect.")
    return wrapped


class Bank:
    def __init__(self):
        self.accounts = {}
        self.last_account_number = 0

    def add_accounts(self, name):
        self.last_account_number += 1
        account = Account(name, self.last_account_number)
        self.accounts[self.last_account_number] = account

    def satna(self, src_acc_num, dest_acc_num, password, value):
        try:
            dest_acc = self.accounts[dest_acc_num]
            src_acc = self.accounts[src_acc_num]
        except KeyError:
            print("id is incorrect")
        else:    
            if src_acc.balance > value:
                src_acc.withdraw(password, value)
                dest_acc.deposit(value)
            else:
                print("value is low.")


class Account:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self._password = "None"
    
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

    @check_pass
    def show_info(self, password):
        print(f"Name: {self.name}, Account number: {self.account_number}, Balance: {self.balance}")

    def deposit(self, value):
        self.balance += value

    @check_pass
    def withdraw(self, password, value):
        self.balance -= value
    


if __name__ == "__main__":
    bank = Bank()
    bank.add_accounts("farhad")
    bank.add_accounts("ali")

    # test password, deposit and withdraw
    bank.accounts[1].password = "Farhad78"
    bank.accounts[1].deposit(20000)
    bank.accounts[1].withdraw("Farhad78", 5000)
    bank.accounts[1].show_info("Farhad78")

    # test satna
    bank.satna(1, 2, "Farhad78", 10000)
    bank.accounts[1].show_info("Farhad78")
    bank.accounts[2].show_info("None")