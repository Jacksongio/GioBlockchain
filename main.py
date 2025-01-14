from blockchain import Blockchain
from users import User


# Initialize the blockchain
my_blockchain = Blockchain()
# sender = "Jack"
# my_blockchain.add_balance(sender, 100)
# Add transactions
Jack = User("Jack", 100)
Jack.to_string()
my_blockchain.add_transaction({"sender": Jack, "recipient": "Troy", "amount": 10})

# Mine transactions
print("Mining...")
my_blockchain.mine_pending_transactions("Miner1")

# Print the blockchain
my_blockchain.print_chain()
