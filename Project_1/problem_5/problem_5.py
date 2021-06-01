import hashlib
import datetime

"""
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. 
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, 
and text strings as the data.
"""


class Blockchain(object):
    """Blockchain implemented as a Singly Linked List"""
    def __init__(self, initial_block=None):
        self.head = initial_block

    def append(self, transaction_data):
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M %m/%d/%Y ")
        new_block = Block(timestamp, transaction_data, 0)

        if self.head is None:
            self.head = new_block
            return

        else:
            block = self.head
            while block.next is not None:
                block = block.next
            block.next = new_block


class Block:
    """Blocks to be appended to Blockchain"""
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        """Function to create unique identifier via sha256 algorithm"""
        sha = hashlib.sha256()
        information = str(self.timestamp) + self.data + str(self.previous_hash)
        hash_str = information.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        """Printing function"""
        return ('Timestamp: {} \n Data: {} \n Previous Hash: {} \nb Hasg: {}'.format(
            self.timestamp, self.data, self.previous_hash, self.hash))


# Test 1
blockchain = Blockchain()
blockchain.append('This is the first block!')
blockchain.append('Yep, this is number two')
blockchain.append('... and number three')
blockchain.append('')
block = blockchain.head
while block is not None:
    print(block)
    block = block.next

# Test 2
b1 = Blockchain()
b1.append("First")
b1.append("Second")
b1.append("Third")
print(b1)               # should print three block data

# Test 3
b2 = Blockchain()
print(b2)               # should print empty because there is no block in b2 chain

# Test 4
b3 = Blockchain()
b3.append("one")
print(b3.head.timestamp)
b3.append("two")
print(b3.head.timestamp)
b3.append("three")
print(b3.head.timestamp)    # all the timestamps are same because they are declared at same time (Hrs:Min)