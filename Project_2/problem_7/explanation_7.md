# HTTPRouter using a Trie
Goal is to implement an HTTPRouter like in a typical web server using the Trie data structure.
There are many different implementations of HTTP Routers such as regular expressions or simple string matching,
but the Trie is an excellent and very efficient data structure for this purpose.
The purpose of an HTTP Router is to take a URL path like "/" or "/about" and figure out what content to return.
In a dynamic web server, the content will often come from a block of code called a handler.
Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /
In addition to a path though, it is necessary to know which function will handle the http request.
In a real router an instance of a class would be passed like Python's SimpleHTTPRequestHandler which would be
responsible for handling requests to that path.
For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler
(root, None) -> ("about", None) -> ("me", "About Me handler")
We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes
We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which
is fine.

## Data Structure


## Efficiency
### Time
+ Add handler method time complexity = O(n): The time complexity is linear dependent to the length of the url input path. 
  The algorithm has to iterate through all elements of the input url.
+ Look up method time complexity = O(n): All elements of the input url have to be iterated through to check if the path 
  exists.

### Space
+ Add handler method space complexity = O(n): For every element in the input url a new TrieNode has to be created.
  Hence, the space complexity is linearly dependent on the input.
+ Look up method space complexity = O(1): No additional memory has to be allocated.