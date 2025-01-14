#users.py

from ecdsa import SigningKey, SECP256k1

class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()
    #sign the transaction
    def sign_transaction(self, transaction_data):
        return self.private_key.sign(transaction_data.encode())
    #adjust the user's balance
    def adjust_balance(self, amount):
        self.amount += amount
    #get the user's balance
    def get_balance(self):
        return self.amount
    #get the user's name
    def get_name(self):
        return self.name
    #this is a simple user class that holds the user's name, amount, private key, and public key
    def to_dict(self):
        return {
            'name': self.name,
            'amount': self.amount,
            'public_key': self.public_key.to_string().hex()
        }
