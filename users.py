# Users class
class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount  # Changed from 0 to 'amount' to use the provided value

    # Function to adjust the balance of a User
    def adjust_balance(self, amount):
        self.amount += amount

    # Function to get the balance of a User
    def get_balance(self):
        return self.amount

    # Function to transfer an amount from one User to another
    def transfer(self, recipient, amount):
        if self.amount >= amount:
            self.amount -= amount
            recipient.adjust_balance(amount)
            return True
        else:
            return False

    # Function to print the details of a User
    def to_string(self):
        print(f"User: {self.name}")
        print(f"Balance: {self.amount}")

    # Function to get the name of the User
    def get_name(self):
        return self.name
