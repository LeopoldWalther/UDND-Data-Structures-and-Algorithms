# HTTPRouter using a Trie

class RouteTrieNode:
    """Represents a single node in a trie"""

    def __init__(self, handler = None):
        """Initialize the node with children plus a handler"""
        self.children = {}
        self.handler = handler

    def insert(self, url_split):
        """Add a child node in this trie node"""
        if url_split not in self.children:
            self.children[url_split] = RouteTrieNode()

#
class RouteTrie:
    """A RouteTrie will store our routes and their associated handlers"""
    def __init__(self, root_handler):
        """Initialize the trie with an root node and a handler, this is the root path or home page node"""
        self.root = RouteTrieNode(root_handler)

    def insert(self, url_elements, handler):
        """Add an URL to the Trie"""
        current_node = self.root

        for url_element in url_elements:
            current_node.insert(url_element)
            current_node = current_node.children[url_element]

        current_node.handler = handler

    def find(self, url_elements):
        """Find the Trie Node that represents this url"""
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for url_element in url_elements:
            if url_element in current_node.children:
                current_node = current_node.children[url_element]
            else:
                return None
        return current_node.handler


class Router:
    """The Router class wraps the trie and handle"""

    def __init__(self, root_handler, not_found_handler = '404 page not found'):
        self.root_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, url, handler):
        """Add a handler for a path"""

        url_elements = self.split_path(url)

        if url_elements is not None:
            self.root_trie.insert(url_elements, handler)

    def lookup(self, url):
        """lookup path (by parts) and return the associated handler"""

        if url is None:
            return None

        url_elements = self.split_path(url)
        url_handler = self.root_trie.find(url_elements)

        if url_handler is None:
            return self.not_found_handler
        else:
            return url_handler

    def split_path(self, url):
        """Splits URL into its elements"""

        if url is None:
            return None
        elif url == '/' or url == '':
            return []

        url_elements = url.split('/')

        return url_elements


print('--------------------given test functions--------------------')
# create the router and add a route
router_1 = Router('root handler', 'not found handler')  # remove the 'not found handler' if you did not implement this
router_1.add_handler('/home/about', 'about handler')  # add a route

print('Pass' if router_1.lookup('/') == 'root handler' else 'Fail')
print('Pass' if router_1.lookup('/home') == 'not found handler' else 'Fail')
print('Pass' if router_1.lookup('/home/about') == 'about handler' else 'Fail')
print('Pass' if router_1.lookup('/home/about/') == 'not found handler' else 'Fail')
print('Pass' if router_1.lookup('/home/about/me') == 'not found handler' else 'Fail')

print('--------------------setting up test router 2--------------------')
router_2 = Router('root handler')
router_2.add_handler('/home/sensors/moisture', 'plants are dry')
router_2.add_handler('/home/automation/ON', 'automated watering activated')
print('Pass')

print('--------------------check for existing routes--------------------')
print('Pass' if router_2.lookup('/home/sensors/moisture') == 'plants are dry' else 'Fail')
print('Pass' if router_2.lookup('/home/automation/ON') == 'automated watering activated' else 'Fail')

print('--------------------check for invalid input--------------------')
print('Pass' if router_2.lookup(None) is None else 'Fail')