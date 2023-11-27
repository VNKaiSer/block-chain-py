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
        self.construct_block(proof_no = 0, previous_hash = 0)
    
    def construct_block(self, proof_no, previous_hash):
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
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return True
    @staticmethod
    def proof_of_work(last_proof):
        proof_no = 0
        while BlockChain.verify_proof(proof_no, last_proof) is False:
            proof_no += 1
        return proof_no
    @property
    def latest_block(self):
        return self.chain[-1]
    @staticmethod
    def verify_proof(proof, last_proof):
        guess = f'{proof}{last_proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    def block_mining(self, detail_miner): 
        
        self.new_data(
            sender="0",
            recipient=detail_miner,
            amount=1
        )
        
        last_block = self.latest_block
        
        last_proof_no = last_block.proof_no
        proof_no = self.proof_of_work(last_proof_no)
        block = self.construct_block(proof_no, last_block.calculate_hash)
        vars(block)['timestamp'] = time.time()
        
    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(block_data):
        #obtains block object from the block data

        return Block(
            block_data['index'],
            block_data['proof_no'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])


# Test blockchain
blockchain = BlockChain()

print("***Mining fccCoin about to start***")
print(blockchain.chain)

last_block = blockchain.latest_block
last_proof_no = last_block.proof_no
proof_no = blockchain.proof_of_work(last_proof_no)

blockchain.new_data(
    sender="0",
    recipient="Quincy Larson",
    amount=
    1,  
)

last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_no, last_hash)

print("***Mining fccCoin has been successful***")
print(blockchain.chain)
    