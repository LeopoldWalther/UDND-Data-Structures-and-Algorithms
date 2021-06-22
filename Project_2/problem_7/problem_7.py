# HTTPRouter using a Trie
# Goal is to implement an HTTPRouter like in a typical web server using the Trie data structure.
# There are many different implementations of HTTP Routers such as regular expressions or simple string matching,
# but the Trie is an excellent and very efficient data structure for this purpose.
# The purpose of an HTTP Router is to take a URL path like "/" or "/about" and figure out what content to return.
# In a dynamic web server, the content will often come from a block of code called a handler.
# Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /
# In addition to a path though, it is necessary to know which function will handle the http request.
# In a real router an instance of a class would be passed like Python's SimpleHTTPRequestHandler which would be
# responsible for handling requests to that path.
# For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler
# (root, None) -> ("about", None) -> ("me", "About Me handler")
# We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes
# We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which
# is fine.

class RouteTrieNode:
    def __init__(self, handler = None):
        """Initialize the node with children as before, plus a handler"""
        self.children = {}
        self.handler = handler

    def insert(self, url_split):
        """Add a child node in this Trie"""
        if url_split not in self.children:
            self.children[url_split] = RouteTrieNode()

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        """Initialize the trie with an root node and a handler, this is the root path or home page node"""
        self.root = RouteTrieNode(root_handler)

    def insert(self, url, handler):
        """Add an URL to the Trie"""
        current_node = self.root
        splitted_url = url.split('/')

        for url_split in splitted_url:
            current_node.insert(url_split)
            current_node = current_node.children[url_split]

        current_node.handler = handler

    def find(self, url):
        """Find the Trie Node that represents this url"""
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        splitted_url = url.split('/')

        for url_split in splitted_url:
            if splitted_url in current_node.children:
                current_node = current_node.children[splitted_url]
            else:
                return None
        return current_node.handler





