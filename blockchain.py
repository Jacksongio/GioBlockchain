# blockchain.py

from block import Block

class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self):
        genesis_block = Block([], "0", self.difficulty)
        genesis_block.mine_block()
        return genesis_block

    def get_latest_block_hash(self):
        return self.chain[-1].hash

    def add_transaction(self, transaction):
        if transaction.verify_signature():
            self.pending_transactions.append(transaction)
            return True
        return False

    def mine_pending_transactions(self, miner_address):
        new_block = Block(self.pending_transactions, self.get_latest_block_hash(), self.difficulty)
        new_block.mine_block()
        self.chain.append(new_block)
        self.pending_transactions = []

    def is_valid_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.previous_hash != previous.hash or current.hash != current.calculate_hash():
                return False
        return True

    def print_chain(self):
        print("📜 Blockchain:")
        for idx, block in enumerate(self.chain):
            print(f"\n🔗 Block {idx}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Nonce: {block.nonce}")
            print("Transactions:")
            for tx in block.transactions:
                print(tx.to_dict() if hasattr(tx, 'to_dict') else tx)
            print("---------------------")
