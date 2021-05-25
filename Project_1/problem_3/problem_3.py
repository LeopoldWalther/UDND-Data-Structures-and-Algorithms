import sys
import heapq


class HuffmannCompressor(object):

    def __init__(self, data=None):
        self.data = data
        self.frequency_dictionary = None
        self.is_encoded = False

    def huffman_encoding(self):
        """Encodes the input string using Huffmann Compression"""
        self.frequency_dictionary = self.determine_character_frequency()

        # create node for each row in table
        min_heap = self.heapify_frequency_dictionary()

        # build and sort list of nodes (minHeap as priority queue)
        # A) pop out two nodes with min frequency from priority queue
        # B) create new node with frequency as sum of two nodes popped out (new Node in Huffmann Tree)
        # C) reinsert new node in priority queue
        # repeat A)-C) until only one element in prio queue
        # assign zero to left, 1 to right
        # traverse Huffmann Tree rfrom root to leaf -> results in binary code
        # change status of is_encoded

        return None, None

    def determine_character_frequency(self):
        """Count frequency of characters in input string called data"""
        frequency_dictionary = dict()
        for character in self.data:
            if character not in frequency_dictionary:
                frequency_dictionary[character] = 1
            else:
                frequency_dictionary[character] += 1
        return frequency_dictionary

    def get_frequency_dictionary(self):
        print(self.frequency_dictionary)

    def heapify_frequency_dictionary(self):
        min_heap = []
        for character, frequency in self.frequency_dictionary.items():
            new_node = HuffmannNode(character, frequency)
            print('Heapifying', new_node.character, new_node.frequency)
            heapq.heappush(min_heap, new_node)
        return min_heap

    def huffman_decoding(self, data, tree):

        if not self.is_encoded:
            return
        # declare a blank decoded string
        # A) pick bit from encoded data, traversing from left to right
        # B) traverse Huffmann Tree from root
        #       if current bit of encoded data = 0 -> move left
        #       else move right
        #       if leaf node: append alphabetical char to decode
        # repeat A)-B) until end
        pass


class HuffmannNode(object):

    def __init__(self, character=None, frequency=None):
        self.left = None
        self.right = None
        self.character = character
        self.frequency = frequency

    def __gt__(self, other):
        if not other:
            return -1
        if not isinstance(other, HuffmannNode):
            return -1
        return self.frequency > other.frequency

    def get_character(self):
        print(self.character)

    def set_left_child(self, Node):
        self.left = Node

    def set_right_child(self, Node):
        self.left = Node

    def has_left_child(self):
        if self.left is None:
            return False
        else:
            return True

    def has_right_child(self):
        if self.right is None:
            return False
        else:
            True


class BinaryTree(object):

    def __init__(self, character=None):
        self.root = HuffmannNode(character)

    def get_root(self):
        return self.root


class MinHeap(object):

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [None] * (self.maxsize + 1)
        self.ROOT = 1  # CONSTANT

    def get_parent(self, position):
        return position // 2

    def get_left_child(self, position):
        return 2 * position

    def get_right_child(self, position):
        return (2 * position) + 1

    def is_leaf(self, position):
        if (self.size // 2) <= position <= self.size:
            return True
        return False

    def swap_nodes(self, first_position, second_position):
        self.heap[second_position], self.heap[first_position] = self.heap[first_position], self.heap[second_position]

    def insert(self, new_node):
        if self.size >= self.maxsize:
            return

        self.size += 1
        self.heap[self.size] = new_node

        current_position = self.size

        while self.heap[current_position].frequency < self.heap[self.get_parent(current_position)].frequency:
            self.swap_nodes(current_position, self.get_parent(current_position))
            current_position = self.get_parent(current_position)

    def remove(self):
        popped = self.heap[self.ROOT]
        self.heap[self.ROOT] = self.heap[self.size]
        self.size -= 1
        self.heapify_node(self.ROOT)
        return popped

    def heapify_node(self, position):
        if not self.is_leaf(position):
            if self.heap[position].frequency > self.heap[self.get_left_child(position)].frequency \
                    or self.heap[position].frequency > self.heap[self.get_right_child(position)].frequency:

                if self.heap[self.get_left_child(position)].frequency < \
                        self.heap[self.get_right_child(position)].frequency:

                    self.swap_nodes(position, self.get_left_child(position))
                    self.heapify_node(self.get_left_child(position))

                else:
                    self.swap_nodes(position, self.get_right_child(position))
                    self.heapify_node(self.get_right_child(position))

    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.heap[i]) + " LEFT CHILD : " +
                  str(self.heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.heap[2 * i + 1]))

    def build_heap(self):
        for position in range(self.size // 2, 0, -1):
            self.heapify_node(position)


class BinaryTree(object):

    def __init__(self, character=None):
        self.root = HuffmannNode(character)

    def get_root(self):
        return self.root


if __name__ == "__main__":
    """
    # test heap
    minHeap = MinHeap(15)
    frequencies = [6, 2, 17, 120, 44, 129, 1, 22, 19]
    for frequency in frequencies:
        node = HuffmannNode('test', frequency)
        minHeap.insert(node)
    minHeap.build_heap()
    minHeap.Print()
    
    # Expected output:  
    #     PARENT : 1 LEFT CHILD : 6 RIGHT CHILD : 2
    #     PARENT : 6 LEFT CHILD : 19 RIGHT CHILD : 44
    #     PARENT : 2 LEFT CHILD : 129 RIGHT CHILD : 17
    #     PARENT : 19 LEFT CHILD : 120 RIGHT CHILD : 22

    print("Min value: " + str(minHeap.remove()))
    # expected output: 1

    minHeap.Print()
    
    # Expected output: 
    #     PARENT : 2 LEFT CHILD : 6 RIGHT CHILD : 17
    #     PARENT : 6 LEFT CHILD : 19 RIGHT CHILD : 44
    #     PARENT : 17 LEFT CHILD : 129 RIGHT CHILD : 22
    #     PARENT : 19 LEFT CHILD : 120 RIGHT CHILD : 22

    print("New Min value: " + str(minHeap.remove()))
    # expected output: 2

    """

    # test Huffmann encoding
    codes = {}
    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffmann_compressor = HuffmannCompressor(a_great_sentence)
    encoded_data, tree = huffmann_compressor.huffman_encoding()
    huffmann_compressor.get_frequency_dictionary()

    """
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    
    """
