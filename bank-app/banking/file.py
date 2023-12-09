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
