import hashlib
import time
# Block class to represent a block in the blockchain
class Block:
    #Constructor for the individual block
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        # Index of the block
        self.index = index
        # Hash of the previous block
        self.previous_hash = previous_hash
        # Data to be stored in the block
        self.transactions = transactions
        #Manually set difficulty
        self.difficulty = 2

        # If timestamp is not provided, it will take the current time
        self.timestamp = timestamp or time.time()
        self.nonce = 0  # Initialize nonce for mining
        # Hash of the block
        self.hash = self.calculate_hash()
        
    # Function to calculate the hash of the block using the index, previous hash, data and timestamp
    # The hash is calculated using the SHA-256 algorithm and is returned as a hexadecimal string
    # The string is encoded to bytes before hashing to avoid any errors
    
    def calculate_hash(self):
        to_hash = f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}"
        return hashlib.sha256(to_hash.encode()).hexdigest()
    
    def mine_block(self, difficulty):
        while not self.hash.startswith("0" * difficulty):
            self.nonce += 1
            
            # Print progress every 10,000 iterations (for example)
            if self.nonce % 10000 == 0:
                print(f"Still mining... nonce = {self.nonce}")
            
            self.hash = self.calculate_hash()
