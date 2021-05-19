# Finding Files
For this problem, the goal is to write code for finding all files under 
a directory and all directories beneath it that end with ".c". 
A path may contain further subdirectories and those subdirectories may 
also contain further subdirectories. 
There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths

## Data Structure
Recursion allows the code to find all files in the directory, as there is 
no limit to the depth of the subdirectories.

I decided to use a list as data structure to save the paths to the files with
the required suffix. A list allows me to append the new paths found by recursive
calls of the function easily.

## Efficiency
### Time
There is a for-loop in the code to check each file found in the list directory
method. This amount of iterations of this for-loop depends on the amount of 
entities found in the current directory. For each recursive call the for-loop
is executed. 
Hence the time complexity of this function is O(n), where n is the amount of
entities in the directory.

### Space
There are two lists used. One list holding all paths to files with the required
suffix and one list holding all entities of the current directory. Both lists
are instantiated for each recursion.
