import sys


def huffman_encoding(data):
    pass


def huffman_decoding(data, tree):
    pass


# heap
class BinaryTreeNode(object):

    def __init__(self, character=None):
        self.left = None
        self.right = None
        self.character = character
        self.frequency = 0

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
        self.root = BinaryTreeNode(character)

    def get_root(self):
        return self.root


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))