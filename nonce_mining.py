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

    def mineBlock(self, difficulty):
        prefix = '0' * difficulty
        print(f"Mining block with difficulty {difficulty} (hash must start with '{prefix}')...")
        start_time = time.time()
        attempts = 0

        while True:
            self.hash = self.calculateHash()
            attempts += 1
            if self.hash.startswith(prefix):
                break
            self.nonce += 1

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Block mined!")
        print(f"Hash: {self.hash}")
        print(f"Nonce: {self.nonce}")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {elapsed_time:.4f} seconds")

# Example usage
difficulty = 4  # You can change this to 5 or 6 to see increased time
block = Block(0, "Proof of Work Simulation", "0")
block.mineBlock(difficulty)
