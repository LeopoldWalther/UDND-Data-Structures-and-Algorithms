# Huffman Compression
In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). 
The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. 
The sender encodes the data, and the receiver decodes the encoded data. 
As part of this problem, I will implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a 
loss (lossy) or no loss (lossless) of information. 
The Huffman Coding is a lossless data compression algorithm. 
There are two phases - encoding and decoding.


The requirements are:
1) lossless compression
2) string input must be handled

Not clear from the requirements:
-  Should upper case and lower case letters be counted as the same? 
   -> I decided to treat upper case and lower case versions of the same letter as different elements as the compression
   is required to be lossless.
   
-  How to treat spaces? -> I decided to treat them as every other character as they hold information.


## Data Structure
I decided to use a min heap as priority queue for the huffman tree. 
Furthermore, I used dictionaries for storing frequency and encoding for each character, so I can use the advantage of 
accessing the information with O(1).

        self.decoded_data = ''
        self.encoded_data = ''
        self.frequency_dictionary = dict()
        self.encoding_dictionary = dict()
        self.min_heap = None
        self.leaf_nodes = None
        self.tree = None

## Efficiency
### Time
Time complexity encode() is =(n*log n)
For the encoding the script has to loop through the complete input data, meaning O(n).
Counting the frequency of each character and storing it into a dictionary means a constant time O(1) inside the for 
loop.
To create the priority list using the min heap, the code hast to loop through the complete dictionary containing the 
frequency and push the created nodes into the min heap, resulting into O(k) where k<=n, as k contains only unique 
characters.
The time complexity of inserting is O(log k).
Therefore O(k*log k) is the overall time complexity of creating the min heap.
Building up the Huffman tree means popping once each element in the min heap O(1) and pushing in merged nodes O(log n)
To encode each character the code has to loop through all the input characters again O(n).

Time complexity for decode() is O(n).
To decode the code has to loop through all input characters.

### Space
The space complexity of encode is O(n) has the space of all variables is linear to the input size.
The space complexity of decode is O(n) where k<n. The text created while encoding is more or less of the size of the 
input.