#main.py

from users import User
from blockchain import Blockchain
from transaction import Transaction

#create users for testing purposes
jack = User("Jack", 100)
miner = User("Miner1", 0)

#initialize blockchain with difficulty level 4
my_blockchain = Blockchain(difficulty=4)

#Jack wants to send 20 to Miner1
transaction_data = f"{jack.public_key.to_string().hex()}{miner.public_key.to_string().hex()}20"
signature = jack.sign_transaction(transaction_data)

#create signed transaction
transaction = Transaction(
    sender_public_key=jack.public_key.to_string().hex(),
    recipient_public_key=miner.public_key.to_string().hex(),
    amount=20,
    signature=signature
)

#add the transaction
my_blockchain.add_transaction(transaction)

#mine pending transactions
my_blockchain.mine_pending_transactions(miner.get_name())

#print the blockchain
my_blockchain.print_chain()
