# Autocomplete with Tries
A trie is a tree-like data structure that stores a dynamic set of strings.
Tries are used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
We will create two classes:
A Trie class that contains the root node (empty string)
A TrieNode class that exposes general functionality of a Trie: inserting a word, finding node which represents  prefix


## Data Structure


## Efficiency
### Time
+ insert method: Time Complexity = O(n), as for each character inserted into the dict, the complexity is O(1)
+ find method: Time Complexity = O(n), as for each character accessed in dict, the complexity is O(1)
+ suffixes method: Time Complexity = O(n), as each character in existing trie has to be accessed with O(1)

### Space
+ insert method: Space Complexity = O(n), as there has to be memory allocated for each character stored
+ find method: Space Complexity = O(1), as there is no memory allocated for accessing the given trie
+ suffixes method: Space Complexity = O(1), as there is no memory allocated for accessing the given trie