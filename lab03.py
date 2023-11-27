import hashlib
import time
class Block: 
    def __init__(self, index, proof_no, previous_hash, data, timestamp =None):
        self.index = index
        self.proof_no = proof_no
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        pass
    @property
    def calculate_hash(self):
        string_hash = "{}{}{}{}{}".format(self.index, self.proof_no, 
                                          self.previous_hash, self.data, 
                                      self.timestamp)
        return hashlib.sha256(string_hash.encode()).hexdigest()
    def __repr__(self):
        return "Block: {}-{}-{}-{}-{}".format(self.index, self.proof_no, 
                                              self.previous_hash, self.data, 
                                              self.timestamp)
class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.contruct_genesis()
        pass
 
    def contruct_genesis(self):
        self.contruct_block(proof_no = 0, previous_hash = 0)
    
    def contruct_block(self, proof_no, previous_hash):
        block = Block(
                        index = len(self.chain), 
                        proof_no = proof_no, 
                        previous_hash = previous_hash, 
                        data = self.current_data)
        self.current_data = []
        self.chain.append(block)
        return block
    
    @staticmethod
    def check_validity(block, prev_block):
        if prev_block.index + 1 != block.index: 
            return False;
        elif prev_block.calculate_hash != block.previous_hash:
            return False
        elif not BlockChain.verify_proof(block.proof_no, prev_block.proof_no):  # type: ignore
            return False
        elif block.timestamp <= prev_block.timestamp: 
            return False
        return True

    def new_data(self, sender, recipient, amount):
        pass
    @staticmethod
    def contruct_proof_of_work():
        pass
    @property
    def last_block(self):
        return self.chain[-1]
    @staticmethod
    def verify_proof(proof, last_proof):
        guess = f'{proof}{last_proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    