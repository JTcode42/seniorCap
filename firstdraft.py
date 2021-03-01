import hashlib
import json

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.name = name # might not need this later
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        
    def hash_block(self):
        
       #Calculates the hash of the block
        
        sha = hashlib.sha256()
        sha.update(self.serialize(['hash']).encode('utf-8'))
        return sha.hexdigest()
        
