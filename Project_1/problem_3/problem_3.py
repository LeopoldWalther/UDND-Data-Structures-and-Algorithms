import sys
import heapq


class HuffmanNode(object):
    """Node Class to be used for Hufman Tree and Min Heap"""
    def __init__(self, character=None, frequency=None):
        self.left = None
        self.right = None
        self.character = character
        self.frequency = frequency

    def __gt__(self, other):
        if not other:
            return -1
        if not isinstance(other, HuffmanNode):
            return -1
        return self.frequency > other.frequency

    def __lt__(self, other):
        if not other:
            return -1
        if not isinstance(other, HuffmanNode):
            return -1
        return self.frequency < other.frequency


class HuffmanCompressor(object):

    def __init__(self):
        self.decoded_data = ''
        self.encoded_data = ''
        self.frequency_dictionary = dict()
        self.encoding_dictionary = dict()
        self.min_heap = None
        self.leaf_nodes = None
        self.tree = None

    def huffman_encoding(self, data):
        """Encodes the input string using Huffman Compression"""

        self.decoded_data = data
        self.encoded_data = ''

        # edge case empty input
        if self.decoded_data == self.encoded_data:
            return self.encoded_data, None

        self.determine_character_frequency()
        self.create_priority_list_from_frequency_dictionary()
        self.create_huffman_tree()
        self.encode_characters_with_huffman_tree()
        self.create_encoded_string()
        huffman_tree = heapq.heappop(self.min_heap)
        return self.encoded_data, huffman_tree

    def determine_character_frequency(self):
        """Counts frequency of characters in input string called data and saves result in dictionary"""
        for character in self.decoded_data:
            if character not in self.frequency_dictionary:
                self.frequency_dictionary[character] = 1
            else:
                self.frequency_dictionary[character] += 1
        return self.frequency_dictionary

    def create_priority_list_from_frequency_dictionary(self):
        """Creates min heap with Huffman nodes from frequency dictionary"""
        self.min_heap = []
        for character, frequency in self.frequency_dictionary.items():
            new_node = HuffmanNode(character, frequency)
            heapq.heappush(self.min_heap, new_node)
        self.leaf_nodes = self.min_heap.copy()

    def create_huffman_tree(self):
        """Creates a Huffman tree from the priority queue"""
        while len(self.min_heap) > 1:
            first_node = heapq.heappop(self.min_heap)
            second_node = heapq.heappop(self.min_heap)
            new_node = HuffmanNode('merged', first_node.frequency + second_node.frequency)
            new_node.left = first_node
            new_node.right = second_node
            heapq.heappush(self.min_heap, new_node)

    def create_encoded_string(self):
        """Creates encoded string by adding all encoded characters into one line"""
        for character in self.decoded_data:
            self.encoded_data += self.encoding_dictionary[character]

    def encode_characters_with_huffman_tree(self):
        """Creates dictionary with encodings per character"""
        separator = ''
        for leaf_node in self.leaf_nodes:
            self.encoding_dictionary[leaf_node.character] = separator.join(
                (self.path_from_root_to_node(self.min_heap[0], leaf_node.character)))

    def path_from_root_to_node(self, root_node, leaf_node_character):
        """Finds the path from root to leaf node in Huffman tree and returns binary code of it"""
        path = self.path_from_node_to_root(root_node, leaf_node_character, [])
        return list(reversed(path))

    def path_from_node_to_root(self, root_node, leaf_node_character, code):
        """Recursive function to find path to leaf node in Huffman binary tree"""
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

    def huffman_decoding(self, data, tree):
        """Decodes data using the Huffman tree"""
        self.encoded_data = data
        self.decoded_data = ''
        self.tree = tree
        self.decoded_data = self.traverse_tree(tree, '')
        return self.decoded_data

    def traverse_tree(self, current_node, text):
        """Traverses the Hufmann tree following the directions as specified by the bits of encoded data"""
        for bit in self.encoded_data:
            if bit == '0':
                current_node = current_node.left
            elif bit == '1':
                current_node = current_node.right

            if current_node.left is None and current_node.right is None:
                text += current_node.character
                current_node = self.tree
        return text


if __name__ == "__main__":

    # test Huffmann encoding

    print('-----------test 1 huffmann encoding-----------')
    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffman_compressor = HuffmanCompressor()
    encoded_data, tree = huffman_compressor.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_compressor.huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print('-----------test 2 huffmann encoding: empty string-----------')
    a_great_sentence = ""
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffman_compressor = HuffmanCompressor()
    encoded_data, tree = huffman_compressor.huffman_encoding(a_great_sentence)

    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_compressor.huffman_decoding(encoded_data, tree)

    print("The content of the encoded data is: {}\n".format(decoded_data))

    print('-----------test 3 huffmann encoding: a lot of characters with low frequency-----------')
    a_great_sentence = "abcdefghijklmnopqrstuvwxyz1234567890?ßäöü"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffman_compressor = HuffmanCompressor()
    encoded_data, tree = huffman_compressor.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_compressor.huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print('-----------test 4 huffmann encoding: long text-----------')
    a_great_sentence = "Who am I? Why am I here?!? What time is it and in what year do I live. Which universe?" \
                       "Can somebody answer my questions, this is nuts!"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffman_compressor = HuffmanCompressor()
    encoded_data, tree = huffman_compressor.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_compressor.huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print('-----------test 5 huffmann encoding: single character repeated-----------')

    a_great_sentence = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA?"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffman_compressor = HuffmanCompressor()
    encoded_data, tree = huffman_compressor.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_compressor.huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))