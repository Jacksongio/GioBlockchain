from blockchain import Blockchain

# Initialize the blockchain
my_blockchain = Blockchain()
# sender = "Jack"
# my_blockchain.add_balance(sender, 100)
# Add transactions
my_blockchain.add_transaction({"sender": "Jack", "recipient": "Troy", "amount": 10})

# Mine transactions
print("Mining...")
my_blockchain.mine_pending_transactions("Miner1")

# Print the blockchain
my_blockchain.print_chain()
