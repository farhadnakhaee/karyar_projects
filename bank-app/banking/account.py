import re
from file import File


def write_file(f):
    """Decorator for writing operation."""
    def wrapper(self, *args):
        f(self, *args)
        self.file.write(f"Func: {f.__name__}, Balance: {self.balance}, at {datetime.now()}\n")
    return wrapper


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
