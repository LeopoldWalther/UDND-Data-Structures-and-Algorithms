# Rearrange Array Elements so as to form two numbers such that their sum is maximum.
# Return these two numbers.
# You can assume that all array elements are in the range [0, 9].
# The number of digits in both the numbers cannot differ by more than 1.
# You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
# for e.g. [1, 2, 3, 4, 5] the expected answer would be [531, 42]. Another expected answer can be [542, 31].
# In scenarios such as these when there are more than one possible answers, return any one.

# sort input list
# go through input list and alternately add element to both output numbers

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_input_list = mergesort(input_list)
    print(sorted_input_list)


def mergesort(items):
    """Mergesort by dividing array into single elements and sorting when merging bac together"""
    # base case
    if len(items) <= 1:
        return items

    # create sub-arrays
    mid_index = len(items) // 2
    left_sub_array = items[:mid_index]
    right_sub_array = items[mid_index:]

    # recursive calls
    left_sub_array = mergesort(left_sub_array)
    right_sub_array = mergesort(right_sub_array)

    return merge(left_sub_array, right_sub_array)


def merge(left_sub_array, right_sub_array):
    """Merges the sub-arrays together from smallest to biggest element"""
    merged = []
    left_index = 0
    right_index = 0

    # go through both sub-array from left to right appending always the smallest element to the merged array
    while left_index < len(left_sub_array) and right_index < len(right_sub_array):
        if left_sub_array[left_index] > right_sub_array[right_index]:
            merged.append(right_sub_array[right_index])
            right_index += 1
        else:
            merged.append(left_sub_array[left_index])
            left_index += 1

    # add what is left in one of the arrays
    merged += left_sub_array[left_index:]
    merged += right_sub_array[right_index:]

    return merged

"""
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
"""


rearrange_digits([4, 6, 2, 5, 9, 8, 7, 3, 0, 1])

# test_function([[1, 2, 3, 4, 5], [542, 31]])
# test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
