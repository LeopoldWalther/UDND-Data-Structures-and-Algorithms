import sys
import heapq


class HuffmannCompressor(object):

    def __init__(self, data=None):
        self.data = data
        self.encoded_data = ''
        self.frequency_dictionary = dict()
        self.encoding_dictionary = dict()
        self.is_encoded = False
        self.min_heap = None
        self.leaf_nodes = None

    def huffman_encoding(self):
        """Encodes the input string using Huffmann Compression"""
        self.determine_character_frequency()
        self.create_priority_list_from_frequency_dictionary()
        self.create_huffmann_tree()
        self.encode_characters_with_huffmann_tree()
        self.create_encoded_string()


        # change status of is_encoded
        print(self.frequency_dictionary)
        print(self.encoding_dictionary)
        print(self.encoded_data)
        print('-------------------')

        return None, None

    def create_encoded_string(self):
        for character in self.data:
            self.encoded_data += self.encoding_dictionary[character]

    def encode_characters_with_huffmann_tree(self):
        separator = ''
        for leaf_node in self.leaf_nodes:
            self.encoding_dictionary[leaf_node.character] = separator.join(
                (self.path_from_root_to_node(self.min_heap[0], leaf_node.character)))

    def path_from_root_to_node(self, root_node, leaf_node_character):
        """Finds the path from root to leaf node in Huffmann tree and returns binary code of it"""
        path = self.path_from_node_to_root(root_node, leaf_node_character, [])
        return list(reversed(path))

    def path_from_node_to_root(self, root_node, leaf_node_character, code):
        """Recursive function to find path to leaf node in Huffmann binary tree"""
        # base cases
        if root_node is None:
            return None
        elif root_node.character == leaf_node_character:
            return code

        # recursion
        left = self.path_from_node_to_root(root_node.left, leaf_node_character, code)
        if left is not None:
            left.append('0')
            return left

        right = self.path_from_node_to_root(root_node.right, leaf_node_character, code)
        if right is not None:
            right.append('1')
            return right
        return None

    def determine_character_frequency(self):
        """Counts frequency of characters in input string called data and saves result in dictionary"""
        for character in self.data:
            if character not in self.frequency_dictionary:
                self.frequency_dictionary[character] = 1
            else:
                self.frequency_dictionary[character] += 1
        return self.frequency_dictionary

    def create_priority_list_from_frequency_dictionary(self):
        """Creates min heap with Huffmann nodes from frequency dictionary"""
        self.min_heap = []
        for character, frequency in self.frequency_dictionary.items():
            new_node = HuffmannNode(character, frequency)
            print('Heapifying', new_node.character, new_node.frequency)
            heapq.heappush(self.min_heap, new_node)
        self.leaf_nodes = self.min_heap.copy()

        """
        Alternative version without heapq library:
        self.min_heap = MinHeap(len(self.frequency_dictionary))
        for character, frequency in self.frequency_dictionary.items():
            new_node = HuffmannNode(character, frequency)
            print('Heapifying', new_node.character, new_node.frequency)
            self.min_heap.insert(new_node)
        """

    def create_huffmann_tree(self):
        """Creates a Huffmann tree from the priority queue"""
        while len(self.min_heap) > 1:
            first_node = heapq.heappop(self.min_heap)
            second_node = heapq.heappop(self.min_heap)
            new_node = HuffmannNode('merged', first_node.frequency + second_node.frequency)
            new_node.left = first_node
            new_node.right = second_node
            heapq.heappush(self.min_heap, new_node)

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

    def __lt__(self, other):
        if not other:
            return -1
        if not isinstance(other, HuffmannNode):
            return -1
        return self.frequency < other.frequency

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
            return True


class BinaryTree(object):

    def __init__(self, character=None):
        self.root = HuffmannNode(character)

    def get_root(self):
        return self.root


class MinHeap(object):

    def __init__(self, maxsize):
        self.maxsize = maxsize * 2
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.ROOT = 1  # CONSTANT

    def get_parent(self, position):
        parent = position // 2
        if parent == 0:
            parent = 1
        return parent

    def get_left_child(self, position):
        return 2 * position

    def get_right_child(self, position):
        return (2 * position) + 1
    # TODO: Check if changing from returning position to returning node

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

        while self.heap[current_position] < self.heap[self.get_parent(current_position)]:
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
            if self.heap[position] > self.heap[self.get_left_child(position)] \
                    or self.heap[position] > self.heap[self.get_right_child(position)]:

                if self.heap[self.get_left_child(position)] < self.heap[self.get_right_child(position)]:

                    self.swap_nodes(position, self.get_left_child(position))
                    self.heapify_node(self.get_left_child(position))  # recursion

                else:
                    self.swap_nodes(position, self.get_right_child(position))
                    self.heapify_node(self.get_right_child(position))  # recursion

    def print_heap(self):
        for i in range(1, (self.size // 2) + 1):
            if not self.heap[2 * i]:
                print(" PARENT : " + str(self.heap[i].frequency) + " LEFT CHILD : None RIGHT CHILD : None")
            elif not self.heap[2 * i + 1]:
                print(" PARENT : " + str(self.heap[i].frequency) + " LEFT CHILD : " +
                      str(self.heap[2 * i].frequency) + " RIGHT CHILD : None")
            else:
                print(" PARENT : " + str(self.heap[i].frequency) + " LEFT CHILD : " +
                      str(self.heap[2 * i].frequency) + " RIGHT CHILD : " + str(self.heap[2 * i + 1].frequency))

    def build_heap(self):
        for position in range(self.size // 2, 0, -1):
            self.heapify_node(position)


class HuffmannTree(object):

    def __init__(self, character=None):
        self.root = HuffmannNode(character)

    def get_root(self):
        return self.root


if __name__ == "__main__":
    """
    # test heap
    print('-----------test heap class-----------')
    minHeap = MinHeap(15)
    frequencies = [6, 2, 17, 120, 44, 129, 1, 22, 19]
    for frequency in frequencies:
        node = HuffmannNode('test', frequency)
        minHeap.insert(node)
    minHeap.build_heap()
    minHeap.print_heap()
    
    # Expected output: 
    
    min_value = minHeap.remove()
    print("Min value: " + str(min_value.frequency))
    # expected output: 1

    minHeap.print_heap()
    
    # Expected output: 

    min_value = minHeap.remove()
    print("New Min value: " + str(min_value.frequency))
    # expected output: 2
    """

    # test Huffmann encoding
    print('-----------test huffmann encoding-----------')
    codes = {}
    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffmann_compressor = HuffmannCompressor(a_great_sentence)
    encoded_data, tree = huffmann_compressor.huffman_encoding()

    """
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    
    """
