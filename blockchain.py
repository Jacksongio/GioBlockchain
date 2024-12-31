import time
import hashlib
# Import the Block class from block.py
from block import Block

'''
Blockchain class to represent the blockchain, which is a list of blocks
It has the following attributes:
    - chain: A list of blocks
    - pending_transactions: A list of transactions that are yet to be added to a block
    - difficulty: The number of leading zeros required in the hash of a block
    - mining_reward: The reward for mining a block
It has the following methods:
    - create_genesis_block: Creates the first block of the blockchain
    - get_latest_block: Returns the last block in the chain
    - add_transaction: Adds a transaction to the pending transactions list
    - mine_pending_transactions: Mines a new block with the pending transactions
    - is_chain_valid: Checks if the blockchain is valid by verifying each block
    - print_chain: Prints the details of each block in the blockchain
'''
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.difficulty = 2
        self.mining_reward = 50
    # Function to create the first block of the blockchain
    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())
    # Function to get the latest block in the chain
    def get_latest_block(self):
        return self.chain[-1]
    # Function to add a transaction to the pending transactions list
    def add_transaction(self, transaction):
        #TO_DO: Append the transaction to the pending transactions list
        #TO_DO: VERIFICATION OF THE TRANSACTION
        self.pending_transactions.append(transaction)
    # Function to mine a new block with the pending transactions
    def mine_pending_transactions(self, miner_address):
        # Create a new block with the pending transactions
        new_block = Block(
            index=len(self.chain),
            previous_hash=self.get_latest_block().hash,
            transactions=self.pending_transactions  # Use 'transactions' to match the Block class
        )
        # Mine the new block
        new_block.mine_block(self.difficulty)
        print(f"Block mined: {new_block.hash}")
        
        # Add the new block to the chain
        self.chain.append(new_block)
        # Reward the miner
        self.pending_transactions = [{"sender": "System", "recipient": miner_address, "amount": self.mining_reward}]

    # Function to check if the blockchain is valid
    def is_chain_valid(self):
        #Check the validity of each block in the chain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            #Check if the hash of the block is valid
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has invalid hash!")
                return False
            #Check if the previous hash of the block is valid
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} has invalid previous hash!")
                return False
        #If all blocks are valid, return True
        return True
    # Function to print the details of each block in the
    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"  Transactions: {block.transactions}")
            print(f"  Hash: {block.hash}")
            print(f"  Previous Hash: {block.previous_hash}\n")
