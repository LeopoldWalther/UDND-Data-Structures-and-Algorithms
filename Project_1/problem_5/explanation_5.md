# Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. 
Each block contains some information and how it is connected related to the other blocks in the chain. 
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. 
For this blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, 
and text strings as the data.

## Data Structure
The individual blocks are implemented as Nodes and the Blockchain as a Singly Linked List.

## Efficiency
### Time
Adding a block to the Blockchain has the complexity of O(n), because the append function has to loop through all 
existing blocks in the singly linked list. I could have implemented it as Doubly Linked List, so the append function
would be linear O(1).

### Space
The space complexity of the Blockchain is O(1).
