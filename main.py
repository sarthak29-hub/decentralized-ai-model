from blockchain import Blockchain
from node import Node

def test_nodes():
    # Initialize Blockchain
    blockchain = Blockchain()

    # Create Nodes
    node1 = Node(node_id="Node1", blockchain=blockchain)
    node2 = Node(node_id="Node2", blockchain=blockchain)

    # Simulate nodes training and submitting updates
    print("Node1 and Node2 will train and submit model updates:")

    node1.train_and_update()
    node2.train_and_update()

    # Aggregate and view the final model
    aggregated_model = blockchain.aggregate_model_updates()
    print(f'Aggregated Model Update: {aggregated_model}')

    # Display the blockchain
    print("\nFinal Blockchain:")
    for block in blockchain.chain:
        print(block)

if __name__ == "__main__":
    test_nodes()
