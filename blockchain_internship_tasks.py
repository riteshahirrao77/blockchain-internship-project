import hashlib
import time
import random

# -----------------------------
# Task 1: Block Class & Tampering Simulation
# -----------------------------
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
        print(f"Time taken: {elapsed_time:.4f} seconds\n")

def displayBlock(block):
    print(f"Index         : {block.index}")
    print(f"Timestamp     : {block.timestamp}")
    print(f"Data          : {block.data}")
    print(f"Previous Hash : {block.previousHash}")
    print(f"Hash          : {block.hash}")
    print(f"Nonce         : {block.nonce}")
    print("-" * 50)

# -----------------------------
# Task 1 Execution
# -----------------------------
print("\n=== Task 1: Block Chaining & Tampering ===")
block0 = Block(0, "Genesis Block", "0")
block1 = Block(1, "Block 1 Data", block0.hash)
block2 = Block(2, "Block 2 Data", block1.hash)
blockchain = [block0, block1, block2]

print("\n--- Blockchain Before Tampering ---")
for block in blockchain:
    displayBlock(block)

print("\n--- Tampering Block 1 Data ---")
block1.data = "Tampered Block 1 Data"
block1.hash = block1.calculateHash()

print("\n--- Blockchain After Tampering ---")
for block in blockchain:
    displayBlock(block)

# -----------------------------
# Task 2: Nonce Mining Simulation
# -----------------------------
print("\n=== Task 2: Nonce Mining Simulation ===")
difficulty = 4  # you can change to 5 or 6 to increase difficulty
mine_block = Block(3, "Mining Difficulty Test", blockchain[-1].hash)
mine_block.mineBlock(difficulty)

# -----------------------------
# Task 3: Consensus Mechanism Simulation
# -----------------------------
print("\n=== Task 3: Consensus Mechanism Simulation ===")

# PoW Mock Validator
miner = {"name": "Miner_A", "power": random.randint(10, 100)}

# PoS Mock Validator
staker = {"name": "Staker_B", "stake": random.randint(10, 100)}

# DPoS Mock Voting
voters = {
    "Voter1": "Delegate_X",
    "Voter2": "Delegate_Y",
    "Voter3": "Delegate_X"
}

def simulate_pow(miner):
    print("=== Proof of Work (PoW) ===")
    print(f"Miner {miner['name']} has computational power: {miner['power']}")
    print(f"Selected validator: {miner['name']} (based on highest power)\n")

def simulate_pos(staker):
    print("=== Proof of Stake (PoS) ===")
    print(f"Staker {staker['name']} has stake amount: {staker['stake']}")
    print(f"Selected validator: {staker['name']} (based on highest stake)\n")

def simulate_dpos(voters):
    print("=== Delegated Proof of Stake (DPoS) ===")
    vote_counts = {}
    for voter, delegate in voters.items():
        print(f"{voter} voted for {delegate}")
        vote_counts[delegate] = vote_counts.get(delegate, 0) + 1

    max_votes = max(vote_counts.values())
    top_delegates = [d for d, v in vote_counts.items() if v == max_votes]
    selected_delegate = random.choice(top_delegates)

    print(f"Selected validator: {selected_delegate} (chosen randomly among top-voted delegates)\n")

simulate_pow(miner)
simulate_pos(staker)
simulate_dpos(voters)
