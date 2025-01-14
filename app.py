#app.py

from flask import Flask, request, render_template, redirect, url_for
from users import User
from transaction import Transaction
from blockchain import Blockchain

app = Flask(__name__)

#initialize your blockchain
my_blockchain = Blockchain(difficulty=4)

# Example users KEEPING THEM IN BECAUSE I WANT TO
jack = User("Jack", 100)
miner = User("Miner1", 0)

@app.route("/", methods=["GET"])
def home():
    """Show the home page (index.html) with forms."""
    return render_template("index.html")
#add transaction
@app.route("/add_transaction", methods=["POST"])
def add_transaction():
    # Get the transaction data from the form
    sender_public_key = request.form.get("sender_public_key")
    recipient_public_key = request.form.get("recipient_public_key")
    amount = request.form.get("amount")
    signature = request.form.get("signature")
    #check for missing fields
    if not (sender_public_key and recipient_public_key and amount and signature):
        return "Missing transaction fields.", 400
    #Check for valid amount
    try:
        amount = int(amount)
    #if the amount is not an integer, return an error
    except ValueError:
        return "Amount must be an integer.", 400

    #create the transaction object
    transaction = Transaction(
        sender_public_key=sender_public_key,
        recipient_public_key=recipient_public_key,
        amount=amount,
        signature=signature
    )

    #attempt to add the transaction (checks 'verify_signature()')
    if my_blockchain.add_transaction(transaction):
        return redirect(url_for("home"))
    else:
        return "Invalid signature. Transaction rejected.", 400
#mine block
@app.route("/mine_block", methods=["POST"])
def mine_block():
    #Get the miners name from the form
    miner_name = request.form.get("miner_name", "Miner1")
    my_blockchain.mine_pending_transactions(miner_name)
    return redirect(url_for("home"))
#view chain
@app.route("/chain", methods=["GET"])
def view_chain():
    #this will now use chain.html which does not use 'enumerate'
    return render_template("chain.html", chain=my_blockchain.chain)
#connect node
if __name__ == "__main__":
    app.run(debug=True, port=5000)
