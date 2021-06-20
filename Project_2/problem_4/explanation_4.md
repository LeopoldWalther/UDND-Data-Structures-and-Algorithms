# Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, the algorithm shall sort the array in a single traversal. 
That without using a sorting function that Python provides.

The idea behind the algorithm designed, is to work with three predefined lists: zeros, ones and twos.
As I know that the input list will only consist of zeros, ones and twos, I can loop through it and append
the elements to either of the three lists. 
At the end I join the three lists to get an ordered list of all given elements.

## Data Structure


## Efficiency
### Time
Time Complexity = O(n)
As the algorithm only loops through the input once, the time complexity is O(n).

### Space
Space Complexity = O(1)
The three lists created, in total are as long as the input. 
Hence the space needed is twice as big as the input size which results into O(1).


