# LRU Cache
Least Recently Used (LRU) cache. 
An LRU cache is a type of cache in which we remove the least recently used 
entry when the cache memory reaches its limit. 
For the current problem, both get and set operations are considered as
use operations.

The requirements are:
1) All operations must take O(1) time.
2) An upper bound must limit the size of the cache. 
3) If the cache is full, and we want to add a new entry to the cache, 
  we remove the least recently used element.

## Data Structure
1) As the operations of set and get are required to take O(1), I decided to use
a dictionary as the Data Structure to store the actual values.
To additionally 
   
2) To be able to monitor if the amount of data stored in the cache reaches its
   maximum capacity, I added a class variable called capacity and a class 
   variable called current_size, both of type integer.
   
3) To keep track of usage of the different elements in the stack I combined
    the dictionary with a doubly linked list. Each node of this doubly linked
    list can be directly accessed with the dictionary.


## Efficieny
### Time
There is no recursion of for-loop in the code. 
All operations are of constant time complexity O(1).

### Space
The following instance variables require memory, when an instance is created.
- self.cache --> A dictionary containing in the worst case as much node elements
  as the variable self.capacity allows 
- self.capacity = capacity --> integer
- self.current_size --> integer
- self.head = None --> a pointer to a Node
- self.tail = None --> a pointer to a Node
