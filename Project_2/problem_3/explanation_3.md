# Rearrange Array Elements
This algorithm needs to rearrange Array Elements so as to form two numbers such that their sum is maximum.
It is safe to assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1.
It is not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
For e.g. [1, 2, 3, 4, 5] the expected answer would be [531, 42]. 
Another expected answer can be [542, 31].
In scenarios such as these when there are more than one possible answers, the algorithm needs to return any one.

The algorithm needs to first sort the given array and then go through the sorted array to alternately add elements
to both output numbers.
I decided to use mergesort for the first step of sorting to ensure time complexity of O(n*log(n)), as with Quicksort
the worst case can be more complex. That I had to pay by a space complexity of O(n).

## Data Structure


## Efficiency
### Time
Time Complexity = O(n*log(n))
Mergesort hast time complexity of O(n*log(n)), to check if the elements are all integers and to create the two output
numbers, each loop has the time complexity of O(n).
This leads to an overall time complexity of O(n*log(n)). 

### Space
Space Complexity = O(n)
The copying of the sub-arrays in merge sort leads to a space complexity of O(n).

