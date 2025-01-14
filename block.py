#block.py

import json
import hashlib
#Block class to represent a block in the blockchain
#Each block has a list of transactions, a previous hash, a nonce, a difficulty, and a hash
#The hash is calculated based on the transactions, previous hash, and nonce
#The nonce is a number that is incremented until the hash meets the difficulty requirement
#The difficulty is the number of zeros that the hash must start with
#The mine_block method is used to mine the block by finding the correct nonce
#The calculate_hash method is used to calculate the hash of the block
class Block:
    def __init__(self, transactions, previous_hash, difficulty):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # New: Nonce for PoW
        self.difficulty = difficulty
        self.hash = self.calculate_hash()
    #calculate the hash of the block
    def calculate_hash(self):
        # Serialize transactions to JSON
        transactions_serializable = [
            tx.to_dict() if hasattr(tx, 'to_dict') else tx
        for tx in self.transactions
        ]
        # Serialize block data to JSON
        block_data = json.dumps({
            'transactions': transactions_serializable,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()
    #mine the block by finding the correct nonce
    def mine_block(self):
        print("⛏️  Mining block...")
        #proof-of-Work: hash must start with 'difficulty' number of zeros
        target = '0' * self.difficulty
        #increment nonce until hash meets difficulty requirement
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
        #print message when block is mined
        print(f"✅ Block mined: {self.hash}")
    #print the block as a string
    def to_string(self):
        print(f"Hash: {self.hash}")
        print(f"Previous Hash: {self.previous_hash}")
        print(f"Nonce: {self.nonce}")
        print("Transactions:")
        for tx in self.transactions:
            print(tx.to_dict())
