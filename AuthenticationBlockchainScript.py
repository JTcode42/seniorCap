import hashlib
import datetime
class Block():
    def __init__(self, index, timestamp, auth, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.auth = auth
        self.previousHash = previousHash
        self.hash = self.hashing()
    
    def hashing(self):
        e = hashlib.sha256()
        e.update(str(self.index).encode('utf-8'))
        e.update(str(self.timestamp).encode('utf-8'))
        e.update(str(self.auth).encode('utf-8'))
        e.update(str(self.previousHash).encode('utf-8'))
        return e.hexdigest()
class authChain():
    def __init__(self): 
        self.blocks = [self.getFirstBlock()]
        self.chain = []
    
    def getFirstBlock(self):
        return Block(0, 
                            datetime.datetime.utcnow(), 
                            'First', 
                            ["User ID","Password"]) 
    
    def addBlock(self, auth):
        self.blocks.append(Block(len(self.blocks), 
                                        datetime.datetime.utcnow(), 
                                        auth, 
                                        self.blocks[len(self.blocks)-1].hash))
        self.chain.append(Block)
    
    def dataVerification(self, Bool=True):
        statement = True
        
        for i in range(1,len(self.blocks)):
            if not self.blocks[i].dataVerification():
                statement = False
                if Bool:
                    print('Incorrect data type: Block '+str(i))
                    
            if self.blocks[i].index != i:
                statement = False
                if Bool:
                    print('Incorrect block index: Block '+str(i))
            
            if self.blocks[i-1].timestamp >= self.blocks[i].timestamp: 
                statement = False
                if Bool:
                    print('Backdated: Block '+str(i))
            
            if self.blocks[i-1].hash != self.blocks[i].previousHash:
                statement = False
                if Bool:
                    print('Incorrect previous hash: Block '+str(i))
            
            if self.blocks[i].hash != self.blocks[i].hashing():
                statement = False
                if Bool:
                    print('Incorrect hash: Block '+str(i))
        
        return statement
        
    def getLength(self):
        return len(self.blocks)-1
