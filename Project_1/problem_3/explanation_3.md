# Huffmann Compression
In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). 
The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. 
The sender encodes the data, and the receiver decodes the encoded data. 
As part of this problem, I will implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a 
loss (lossy) or no loss (lossless) of information. 
The Huffman Coding is a lossless data compression algorithm. 
There are two phases - encoding and decoding.

A. Huffman Encoding
Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. 
The string message can be an unsorted one as well. 
We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data. 
The following steps illustrate the Huffman encoding:
1)..



The requirements are:
1) ...

Not clear from the requirements:
-  Should upper case and lower case letters be counted as the same? 
   -> I decided to treat upper case and lower case versions of the same letter as different elements as the compression
   is required to be lossless.


## Data Structure


## Efficiency
### Time


### Space

