import sys


def huffman_encoding(data):
    pass


def huffman_decoding(data, tree):
    pass


class MinHeap(object):

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
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

    def swap(self, first_position, second_position):
        self.heap[second_position], self.heap[first_position] = self.heap[first_position], self.heap[second_position]

    def insert(self, element):
        if self.size >= self.maxsize:
            return

        self.size += 1
        self.heap[self.size] = element

        current_position = self.size

        while self.heap[current_position] < self.heap[self.get_parent(current_position)]:
            self.swap(current_position, self.get_parent(current_position))
            current_position = self.get_parent(current_position)

    def remove(self):
        popped = self.heap[self.ROOT]
        self.heap[self.ROOT] = self.heap[self.size]
        self.size -= 1
        self.heapify_node(self.ROOT)
        return popped

    def heapify_node(self, position):
        if not self.is_leaf(position):
            if self.heap[position] > self.heap[self.get_left_child(position)] or self.heap[position] > self.heap[self.get_right_child(position)]:
                if self.heap[self.get_left_child(position)] < self.heap[self.get_right_child(position)]:
                    self.swap(position, self.get_left_child(position))
                    self.heapify_node(self.get_left_child(position))

                else:
                    self.swap(position, self.get_right_child(position))
                    self.heapify_node(self.get_right_child(position))

    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.heap[i])+" LEFT CHILD : "+
                  str(self.heap[2 * i])+" RIGHT CHILD : "+
                  str(self.heap[2 * i + 1]))

    def build_heap(self):
        for position in range(self.size//2, 0, -1):
            self.heapify_node(position)


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

    # test heap
    minHeap = MinHeap(15)
    values = [6, 2, 17, 120, 44, 129, 1, 22, 19]
    for value in values:
        minHeap.insert(value)
    minHeap.build_heap()
    minHeap.Print()
    """
    Expected output:  
        PARENT : 1 LEFT CHILD : 6 RIGHT CHILD : 2
        PARENT : 6 LEFT CHILD : 19 RIGHT CHILD : 44
        PARENT : 2 LEFT CHILD : 129 RIGHT CHILD : 17
        PARENT : 19 LEFT CHILD : 120 RIGHT CHILD : 22
    """
    print("Min value: " + str(minHeap.remove()))
    # expected output: 1

    minHeap.Print()
    """
    Expected output: 
        PARENT : 2 LEFT CHILD : 6 RIGHT CHILD : 17
        PARENT : 6 LEFT CHILD : 19 RIGHT CHILD : 44
        PARENT : 17 LEFT CHILD : 129 RIGHT CHILD : 22
        PARENT : 19 LEFT CHILD : 120 RIGHT CHILD : 22
    """


    print("New Min value: " + str(minHeap.remove()))
    # expected output: 2

    
    """

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
    
    """