# node.py

from flask import Flask, request, jsonify
from blockchain import Blockchain
from transaction import Transaction
import requests

app = Flask(__name__)

# Initialize a blockchain for this node
blockchain = Blockchain(difficulty=4)
peers = set()  # Set to store peer nodes

# 🔗 Endpoint to get the blockchain
@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.to_string() for block in blockchain.chain]
    return jsonify(chain_data), 200

# ➕ Endpoint to add new transactions
@app.route('/transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    required_fields = ['sender_public_key', 'recipient_public_key', 'amount', 'signature']
    
    if not all(field in data for field in required_fields):
        return "Invalid transaction data.", 400

    transaction = Transaction(
        data['sender_public_key'],
        data['recipient_public_key'],
        data['amount'],
        data['signature']
    )

    if blockchain.add_transaction(transaction):
        broadcast_transaction(data)
        return "Transaction added and broadcasted.", 201
    else:
        return "Invalid transaction signature.", 400

# 🏗️ Endpoint to mine a block
@app.route('/mine', methods=['GET'])
def mine_block():
    blockchain.mine_pending_transactions("Miner1")
    broadcast_block(blockchain.chain[-1])
    return "Block mined and broadcasted!", 200

# 🌐 Endpoint to connect new peers
@app.route('/connect', methods=['POST'])
def connect_node():
    data = request.get_json()
    peers.update(data.get("peers", []))
    return "Peers connected.", 200

# 📨 Broadcast transaction to peers
def broadcast_transaction(transaction_data):
    for peer in peers:
        try:
            requests.post(f"{peer}/transaction", json=transaction_data)
        except Exception as e:
            print(f"Failed to broadcast transaction to {peer}: {e}")

# 📨 Broadcast mined block to peers
def broadcast_block(block):
    block_data = {
        'transactions': [tx.to_dict() for tx in block.transactions],
        'previous_hash': block.previous_hash,
        'hash': block.hash,
        'nonce': block.nonce
    }
    for peer in peers:
        try:
            requests.post(f"{peer}/block", json=block_data)
        except Exception as e:
            print(f"Failed to broadcast block to {peer}: {e}")

if __name__ == '__main__':
    import sys
    port = 5000 if len(sys.argv) < 2 else int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
