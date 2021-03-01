import hashlib
import json

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.name = name # might not need this later
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        
        
