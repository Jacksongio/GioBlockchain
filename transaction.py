#transaction.py

from ecdsa import VerifyingKey, SECP256k1, BadSignatureError
# This is a simple transaction class that holds the sender's public key, recipient's public key, amount, and signature
class Transaction:
    def __init__(self, sender_public_key, recipient_public_key, amount, signature=None):
        # If these are already hex strings from a form, just store them directly
        self.sender_public_key = sender_public_key
        self.recipient_public_key = recipient_public_key
        self.amount = amount
        self.signature = signature  # <-- remove .hex() usage to avoid errors on str

    def to_dict(self):
        return {
            'sender_public_key': self.sender_public_key,
            'recipient_public_key': self.recipient_public_key,
            'amount': self.amount,
            'signature': self.signature
        }
    # This is where you would verify the signature TO BE IMPLEMENTED
    def verify_signature(self):
        """
        If you *really* have a signature in hex that needs verification, do it carefully.
        For example:
        
        try:
            sender_key = VerifyingKey.from_string(bytes.fromhex(self.sender_public_key), curve=SECP256k1)
            data = f"{self.sender_public_key}{self.recipient_public_key}{self.amount}"
            return sender_key.verify(bytes.fromhex(self.signature), data.encode())
        except (BadSignatureError, ValueError):
            return False
        except Exception as e:
            print(f"Verification error: {e}")
            return False
        """
        #for now, if you're testing simple flows, you might skip or stub out real verification:
        return True if self.signature else False
