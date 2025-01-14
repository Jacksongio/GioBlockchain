# transaction.py

from ecdsa import VerifyingKey, SECP256k1, BadSignatureError

class Transaction:
    def __init__(self, sender_public_key, recipient_public_key, amount, signature=None):
        # Ensure public keys are hex strings
        self.sender_public_key = sender_public_key.hex() if isinstance(sender_public_key, bytes) else sender_public_key
        self.recipient_public_key = recipient_public_key.hex() if isinstance(recipient_public_key, bytes) else recipient_public_key
        self.amount = amount
        self.signature = signature.hex() if signature else None

    def to_dict(self):
        return {
            'sender_public_key': self.sender_public_key,
            'recipient_public_key': self.recipient_public_key,
            'amount': self.amount,
            'signature': self.signature
        }

    def verify_signature(self):
        if self.signature is None:
            return False

        try:
            # Ensure public key is passed as a string to from_string
            sender_key = VerifyingKey.from_string(bytes.fromhex(self.sender_public_key), curve=SECP256k1)
            data = f"{self.sender_public_key}{self.recipient_public_key}{self.amount}"
            return sender_key.verify(bytes.fromhex(self.signature), data.encode())
        except BadSignatureError:
            return False
        except Exception as e:
            print(f"Error during signature verification: {e}")
            return False
