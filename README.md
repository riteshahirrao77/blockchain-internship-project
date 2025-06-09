  Blockchain Internship Mini Project

This repository contains code for a blockchain-based simulation assigned during my internship. It includes three mini tasks that demonstrate core blockchain concepts: block creation and tampering, proof-of-work mining, and consensus mechanisms (PoW, PoS, DPoS).

---

✅ Tasks Completed

 1. Block Simulation in Code
- Created a `Block` class with:
  - `index`, `timestamp`, `data`, `previousHash`, `hash`, `nonce`
- Linked 3 blocks using `previousHash`
- Displayed all blocks and their hashes
- Simulated tampering of Block 1 and showed how following blocks become invalid

 2. Nonce Mining Simulation
- Implemented a `mineBlock(difficulty)` method
- Simulated Proof-of-Work by adjusting the nonce until the block’s hash started with `"0000"`
- Measured:
  - Total nonce attempts
  - Time taken to mine the block

 3. Consensus Mechanism Simulation
Simulated three different consensus logics:
- PoW (Proof-of-Work) — Validator chosen based on computational power
- PoS (Proof-of-Stake) — Validator chosen based on stake amount
- DPoS (Delegated Proof-of-Stake)— Validator elected via voting by 3 mock accounts



