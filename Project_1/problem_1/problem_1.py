class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):
    """Least Recently Used (LRU) cache"""

    def __init__(self, capacity):  # all operations are of O(1)
        """Initialize class variables"""
        if capacity <= 0:
            print('The capacity of the LRU Cache should be a positive integer.')
            return None
        self.cache = dict()
        self.capacity = capacity
        self.current_size = 0
        self.head = None
        self.tail = None

    def get(self, key):  # all operations are of O(1)
        """Retrieve item from provided key. Return -1 if nonexistent"""
        if key in self.cache:  # cache hit -> return value
            new_node = self.cache[key]
            self.update_least_recently_used_list(new_node)
            return new_node.value
        else:  # cache miss -> -1
            return -1

    def set(self, key, value):  # all operations are of O(1)
        """Set the value if the key is not present in the cache"""
        new_node = Node(value)
        if key not in self.cache:
            self.set_new_head(new_node)
            self.set_cache(key, new_node)
        else:  # when key already exists, only move up in least recently used list
            self.update_least_recently_used_list(new_node)

    def update_least_recently_used_list(self, new_node):  # all operations are of O(1)
        """
        For get and set methods moves the least recent used value to head of the doubly linked list.
        If a new_node is given to this function it is tested that it already is part of the linked list
        """
        # delete node from current position
        if self.current_size == 1:
            self.head = None
            self.tail = None
        elif new_node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif new_node == self.tail:  # if node is at tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:  # if node is not at tail
            prev_node = new_node.prev
            next_node = new_node.next
            prev_node.next = next_node
            next_node.prev = prev_node

        # make used node head
        self.set_new_head(new_node)

    def set_cache(self, key, new_node):  # all operations are of O(1)
        """Append element to Doubly Linked List"""
        self.cache[key] = new_node
        self.current_size += 1

    def set_new_head(self, new_node):  # all operations are of O(1)
        if not self.capacity_available():
            self.delete_least_recent_used()

        # if no Node in List, make new Node head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if List not empty, add new Node to head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def capacity_available(self):  # all operations are of O(1)
        """Check if amount of elements lower than capacity"""
        if self.current_size < self.capacity:
            return True
        else:
            return False

    def delete_least_recent_used(self):  # all operations are of O(1)
        """Delete last element of Doubly Linked List"""
        deletion_node = self.tail
        del self.cache[deletion_node.value]
        self.current_size -= 1
        self.tail = self.tail.prev
        self.tail.next = None


# Test 1:
our_cache = LRU_Cache(5)  # initialize class
our_cache.set(1, 1)  # fill cache
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print('Output:', our_cache.get(1), '- Expected output: 1')
# returns 1

print('Output:', our_cache.get(2), '- Expected output: 2')
# returns 2

print('Output:', our_cache.get(9), '- Expected output: -1, because 9 is not present in the cache')
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)  # deletes 3

print('Output:', our_cache.get(3), '- Expected output: -1, as cache reached max capacity and 3 was the LRU')
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache.set(345678909876543234567, 345678909876543234567)
print('Output:', our_cache.get(345678909876543234567), '- Expected output: 345678909876543234567')
# returns 345678909876543234567
print('Output:', our_cache.get(4), '- Expected output: -1, as cache reached max capacity and 4 was the LRU')
# returns 4

print('Output:', our_cache.get(5), '- Expected output: 5')
# returns -1


# Test 2:
our_cache = LRU_Cache(900000)  # initialize class
our_cache.set(1, 1)  # fill cache
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print('Output:', our_cache.get(1), '- Expected output: 1')
# returns 1

print('Output:', our_cache.get(2), '- Expected output: 2')
# returns 2

print('Output:', our_cache.get(9), '- Expected output: -1, because 9 is not present in the cache')
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)  # deletes 3

print('Output:', our_cache.get(3), '- Expected output: -1, as cache reached max capacity and 3 was the LRU')
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache.set(345678909876543234567, 345678909876543234567)
print('Output:', our_cache.get(345678909876543234567), '- Expected output: 345678909876543234567')
# returns 345678909876543234567
print('Output:', our_cache.get(4), '- Expected output: -1, as cache reached max capacity and 4 was the LRU')
# returns 4

print('Output:', our_cache.get(5), '- Expected output: 5')
# returns -1



# Test 2:
our_cache = LRU_Cache(-1)  # initialize class


# Test 3:
our_cache = LRU_Cache(-1)  # initialize class

