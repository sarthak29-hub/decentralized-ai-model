import hashlib
import time
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new Block and adds it to the chain
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) if self.chain else '1',
        }

        # Now calculate the hash of the block
        block['hash'] = self.hash(block)

        # Add the block to the chain
        self.chain.append(block)
        
        # Reset current transactions
        self.current_transactions = []
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1 if self.chain else 1

    @staticmethod
    def hash(block):
        """
        Returns the hash of a block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1] if self.chain else None

    def aggregate_model_updates(self):
        """
        Aggregate all model updates from transactions in the blockchain
        For simplicity, it calculates the average of all updates
        """
        total_update = 0
        update_count = 0
        for block in self.chain:
            for transaction in block['transactions']:
                total_update += transaction['amount']
                update_count += 1
        if update_count > 0:
            return total_update / update_count
        return 0
