import random

# Mock Validators
miner = {"name": "Miner_A", "power": random.randint(10, 100)}
staker = {"name": "Staker_B", "stake": random.randint(10, 100)}
voters = {
    "Voter1": "Delegate_X",
    "Voter2": "Delegate_Y",
    "Voter3": "Delegate_X"
}

# ----- Proof of Work (PoW) -----
def simulate_pow(miner):
    print("=== Proof of Work (PoW) ===")
    print(f"Miner {miner['name']} has computational power: {miner['power']}")
    print(f"Selected validator: {miner['name']} (based on highest power)")
    print()

# ----- Proof of Stake (PoS) -----
def simulate_pos(staker):
    print("=== Proof of Stake (PoS) ===")
    print(f"Staker {staker['name']} has stake amount: {staker['stake']}")
    print(f"Selected validator: {staker['name']} (based on highest stake)")
    print()

# ----- Delegated Proof of Stake (DPoS) -----
def simulate_dpos(voters):
    print("=== Delegated Proof of Stake (DPoS) ===")
    vote_counts = {}
    for voter, delegate in voters.items():
        print(f"{voter} voted for {delegate}")
        vote_counts[delegate] = vote_counts.get(delegate, 0) + 1

    max_votes = max(vote_counts.values())
    top_delegates = [d for d, v in vote_counts.items() if v == max_votes]
    selected_delegate = random.choice(top_delegates)

    print(f"Selected validator: {selected_delegate} (chosen randomly among top-voted delegates)")
    print()

# ----- Run All Simulations -----
simulate_pow(miner)
simulate_pos(staker)
simulate_dpos(voters)
