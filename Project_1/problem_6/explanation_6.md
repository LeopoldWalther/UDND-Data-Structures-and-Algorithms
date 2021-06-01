# Union and Intersection of Two Linked Lists
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. 
The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both 
the sets A and B.

## Data Structure
- Union: The linked lists get cloned, so that other functions using the same input are not affected.
- Intersection: A dictionary is created to keep track of the appearences. 

## Efficiency
### Time
- Union: O(n) - To create clones of the both input linked lists, the code loops through both of them O(n).
  After that the code loops through the copy of the first linked list in order to connect it to the clone 
  of the second linked list. One loop could be omitted by using the loop of creating a clone to also give
  back the last node of the linked list.
- Intersection: O(n) - To create the dictionary the code has to loop through both input linked lists O(n).
  After that the code has to loop through the dictionary to check which keys have the expected values.

### Space
- Union: O(n) Each linked list is cloned/copied once.
- Intersection: O(n) Each linked list is copied into the dictionary. 