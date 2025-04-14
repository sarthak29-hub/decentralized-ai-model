import time
import random
import numpy as np
from blockchain import Blockchain
from ml_model import SimpleModel

class Node:
    def __init__(self, node_id, blockchain):
        self.node_id = node_id
        self.blockchain = blockchain

    def generate_training_data(self):
        """
        Generate dummy training data for simulation
        X: features, y: labels
        """
        X = np.random.rand(50, 2) * 10  # 50 samples, 2 features
        y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(50)  # Linear relation with noise
        return X, y

    def train_model(self):
        """
        Train the model and get learned weights and bias
        """
        X, y = self.generate_training_data()
        model = SimpleModel()
        return model.train(X, y)  # Returns dict with weights and bias

    def submit_model_update(self):
        """
        Submit the trained model parameters to the blockchain
        """
        model_update = self.train_model()
        print(f"Node {self.node_id} submitting model update: {model_update}")
        self.blockchain.new_transaction(
            sender=self.node_id,
            recipient="Blockchain",
            amount=model_update
        )

    def mine_block(self):
        """
        Mine a new block after training
        """
        proof = random.randint(10000, 99999)
        previous_hash = self.blockchain.hash(self.blockchain.last_block)
        self.blockchain.new_block(proof, previous_hash)

    def train_and_update(self):
        """
        Perform training and update blockchain
        """
        self.submit_model_update()
        self.mine_block()
