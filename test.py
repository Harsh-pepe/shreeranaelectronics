import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Genesis block
genesis_block = Block(0, "0", "Genesis Block")
print(f"Genesis Block Hash: {genesis_block.hash}")

# Adding another block
block1 = Block(1, genesis_block.hash, "Block 1 Data")
print(f"Block 1 Hash: {block1.hash}")
