# users.py

from ecdsa import SigningKey, SECP256k1

class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def sign_transaction(self, transaction_data):
        return self.private_key.sign(transaction_data.encode())

    def adjust_balance(self, amount):
        self.amount += amount

    def get_balance(self):
        return self.amount

    def get_name(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name,
            'amount': self.amount,
            'public_key': self.public_key.to_string().hex()
        }
