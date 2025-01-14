# block.py

import json
import hashlib

class Block:
    def __init__(self, transactions, previous_hash, difficulty):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # New: Nonce for PoW
        self.difficulty = difficulty
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transactions_serializable = [
            tx.to_dict() if hasattr(tx, 'to_dict') else tx
        for tx in self.transactions
        ]
        block_data = json.dumps({
            'transactions': transactions_serializable,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self):
        print("⛏️  Mining block...")
        # Proof-of-Work: hash must start with 'difficulty' number of zeros
        target = '0' * self.difficulty

        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f"✅ Block mined: {self.hash}")

    def to_string(self):
        print(f"Hash: {self.hash}")
        print(f"Previous Hash: {self.previous_hash}")
        print(f"Nonce: {self.nonce}")
        print("Transactions:")
        for tx in self.transactions:
            print(tx.to_dict())
