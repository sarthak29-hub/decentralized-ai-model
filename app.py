# app.py
from flask import Flask, jsonify, request
import uuid
from node import Node
from blockchain import Blockchain

node_identifier = str(uuid.uuid4()).replace('-', '')[:6]
app = Flask(__name__)

blockchain = Blockchain()
node = Node(node_identifier, blockchain)

@app.route('/train', methods=['GET'])
def train():
    node.train_and_update()
    return jsonify({'message': f'Model update from {node.node_id} submitted and block mined.'}), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/model', methods=['GET'])
def get_aggregated_model():
    aggregated_weights = blockchain.aggregate_model_updates()
    return jsonify({
        'aggregated_weights': aggregated_weights,
        'message': 'This is the aggregated model from the blockchain.'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)