import datetime
import hashlib
import random
import sys

class Block:
    blockNum = 0
    hashRand = 0 # one-time use value
    prev = 0x0
    info = None
    next = None
    hash = None
    time = datetime.datetime.now()

    def __init__(self, info):
        self.info = info

    def hashCreate(self):
        hashVals = hashlib.sha256()
        hashVals.update(
        str(self.hashRand).encode('utf-8') + # encoding Unicode letters
        str(self.info).encode('utf-8') +
        str(self.prev).encode('utf-8') +
        str(self.time).encode('utf-8') +
        str(self.blockNum).encode('utf-8')
        )
        return hashVals.hexdigest() # encoded data in hexadecimal format

    def __str__(self): # output
        return "Block Hash: " + str(self.hashCreate()) + "\nBlock Number: " + str(self.blockNum) + "\nBlock Data: " + str(self.info) + "\nHashes: " + str(self.hashRand) + "\n-----------"

class Blockchain:
    diff = int(sys.argv[1])
    hashRand_Max = 2 ** 32 # internal block size for SHA256 is 32 bits
    end = 2 ** (256 - diff)

    block = Block("Start")
    temp = beginning = block

    def add(self, block):
        block.prev = self.block.hashCreate()
        block.blockNum = self.block.blockNum + 1
        self.block.next = block
        self.block = self.block.next

    def mining(self, block):
        for n in range(self.hashRand_Max):
            if (int(block.hashCreate(), 16) <= self.end):
                self.add(block)
                print("Proof-of-work is accepted") #Proof-of-work since we can verify the value of the hash in the conditional
                print(block)
                break
            else:
                block.hashRand = block.hashRand + 1

chain = Blockchain()

for n in range(1, 11):
    chain.mining(Block("Block " + str(n)))
