# Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search.
If found in the array return its index, otherwise return -1.
You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

The idea of the algorithm is divide & conquer: 
The algorithm receives an array to be searched, a target value and the start and end indexes to search in the array. 
The array given must be a sorted array which is rotated at some random pivot point.
The algorithm finds the middle index between given start and end. 
It uses the fact that because of the rotation of the array the following must not be true for all sub-arrays: 
array[start] < array[mid] < array[end].
First it checks if the value at the starting index is smaller than the value in the middle, if so the target value
has to be between starting and middle index if the target value is bigger at the value in the starting index, but
smaller than the value at the middle index.
If that is not the case, the value has to be between the middle index and the ending index. 
The algorithm recursively calls itself for the chosen sub-array.
If the value at the starting index is not smaller than the value in the middle, a analogues logic is applied for the
case that the value at the end index of the array is bigger than the value in the middle.

## Data Structure


## Efficiency
### Time
Time Complexity = O(log(n))
...

### Space
Space Complexity = O(1)
...



