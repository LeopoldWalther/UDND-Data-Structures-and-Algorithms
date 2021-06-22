# A trie is a tree-like data structure that stores a dynamic set of strings.
# Tries are used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# We will create two classes:
# A Trie class that contains the root node (empty string)
# A TrieNode class that exposes general functionality of a Trie: inserting a word, finding node which represents  prefix

class TrieNode(object):
    """Represents a single node in the Trie"""

    def __init__(self):
        """Initialize this node in the Trie"""
        self.is_word = False
        self.children = {}

    def insert(self, char):
        """Add a child node in this Trie"""
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        """Recursive function that collects the suffix for all complete words below this point"""

        suffixes = list()

        for char, node in self.children.items():
            if node.is_word is True:
                suffixes.append(suffix + char)
            if node.children:
                suffixes += node.suffixes(suffix + char)

        return suffixes


class Trie(object):
    """The Trie itself containing the root node and insert/find functions"""

    def __init__(self):
        """Initialize this Trie (add a root node)"""
        self.root = TrieNode()

    def insert(self, word):
        """Add a word to the Trie"""

        current_node = self.root

        for char in word:
            current_node.insert(char)

            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        """Find the Trie node that represents this prefix"""

        current_node = self.root

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None

        return current_node


print('--------------------start tests--------------------')

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

print('--------------------insert function--------------------')
for word in wordList:
    MyTrie.insert(word)
print('pass')

print('--------------------find function--------------------')
assert type(MyTrie.find('f')) is TrieNode
assert type(MyTrie.find('a')) is TrieNode
assert type(MyTrie.find('ant')) is TrieNode
assert type(MyTrie.find('trigonometry')) is TrieNode
assert type(MyTrie.find('')) is TrieNode

assert MyTrie.find('g') is None
assert MyTrie.find('x') is None
print('pass')

print('--------------------suffixes function--------------------')
test_node_1 = MyTrie.find('f')
assert test_node_1.suffixes() == ['un', 'unction', 'actory']

test_node_2 = MyTrie.find('trigonomet')
assert test_node_2.suffixes() == ['ry']

test_node_3 = MyTrie.find('trigonometry')
assert test_node_3.suffixes() == []

test_node_4 = MyTrie.find('')
assert test_node_4.suffixes() == [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
print('pass')