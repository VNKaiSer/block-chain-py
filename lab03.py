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
 
    def contruct_genesis():
        pass
    
    @staticmethod
    def check_validity():
        pass
    def new_data(self, sender, recipient, amount):
        pass
    @staticmethod
    def contruct_proof_of_work():
        pass
    @property
    def last_block(self):
        return self.chain[-1]
    