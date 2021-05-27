# Huffman Compression
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. 
We can construct this hierarchy as such. 
Where User is represented by str representing their id

Goal is to write a function that provides an efficient look up of whether the user is in a group.

## Data Structure
I created a recursive function to solve that problem, as the folder structure is recursive as well.
The function starts at the group given and checks if the user string is in the user list,
if not it goes recursively through the list of groups of the given group by calling itself for each group found.

## Efficiency
### Time
The time complexity is O(n) as there is one for loop to go through the groups in the list of groups for the recursive
calls. In each call there can be a loop as well, still it is O(n).

### Space
Space complexity is O(1) as there is are only variables created that have the size of the given objects.