import hashlib
import time

class Block:
    def __init__(self, index, data, previousHash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        value = f"{self.index}{self.timestamp}{self.data}{self.previousHash}{self.nonce}"
        return hashlib.sha256(value.encode()).hexdigest()

def displayBlock(block):
    print(f"Index         : {block.index}")
    print(f"Timestamp     : {block.timestamp}")
    print(f"Data          : {block.data}")
    print(f"Previous Hash : {block.previousHash}")
    print(f"Hash          : {block.hash}")
    print(f"Nonce         : {block.nonce}")
    print("-" * 50)

# Create 3 blocks
block0 = Block(0, "Genesis Block", "0")
block1 = Block(1, "Block 1 Data", block0.hash)
block2 = Block(2, "Block 2 Data", block1.hash)

# Store in chain
blockchain = [block0, block1, block2]

print("=== Blockchain Before Tampering ===")
for block in blockchain:
    displayBlock(block)

# Tampering with Block 1
print("\n=== Tampering Block 1's Data ===")
block1.data = "Tampered Block 1 Data"
block1.hash = block1.calculateHash()

print("=== Blockchain After Tampering ===")
for block in blockchain:
    displayBlock(block)
