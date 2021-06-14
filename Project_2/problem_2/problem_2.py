# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be O(log n).
# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4


def rotated_array_search(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array): a sorted array which is rotated at some random pivot point
       target(int): target value to find in array
    Returns:
       int: Index or -1
    """
    if target is None or input_list is None:
        return -1

    return rotated_array_search_recursive(input_list, target, 0, len(input_list)-1)


def rotated_array_search_recursive(input_list, target, start, end):
    """
    The idea of this function is divide & conquer: The algorithm receives an array to be searched, a target value
    and the start and end indexes to search in the array. The array given must be a a sorted array which is rotated at
    some random pivot point.
    The algorithm finds the middle index between given start and end. It uses the fact that because of the rotation of
    the array the following must not be true for all sub-arrays: array[start] < array[mid] < array[end].
    First it checks if the value at the starting index is smaller than the value in the middle, if so the target value
    has to be between starting and middle index if the target value is bigger at the value in the starting index, but
    smaller than the value at the middle index. If that is not the case, the value has to be between the middle index
    and the ending index. The algorithm recursively calls itself for the chosen sub-array.
    If the value at the starting index is not smaller than the value in the middle, a analogues logic is applied for the
    case that the value at the end index of the array is bigger than the value in the middle.

    Args:
        input_list: a sorted array which is rotated at some random pivot point
        target: target value to find in array
        start: starting index to search in array
        end: ending index to search in array

    Returns:
    """

    if start > end:
        return -1

    mid = (start + end) // 2

    if input_list[mid] == target:
        return mid

    if input_list[start] <= input_list[mid]:  # then left side ordered
        if input_list[start] <= target < input_list[mid]:  # then target value on left side
            return rotated_array_search_recursive(input_list, target, start, mid-1)
        else:  # then target value in right side
            return rotated_array_search_recursive(input_list, target, mid+1, end)

    elif input_list[end] >= input_list[mid]:  # then right side ordered
        if input_list[end] >= target > input_list[mid]:  # then target value in right side
            return rotated_array_search_recursive(input_list, target, mid+1, end)
        else:
            return rotated_array_search_recursive(input_list, target, start, mid-1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# given test functions
print('--------------------given test functions--------------------')
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# long array
print('-------------------long array---------------------')
test_function([[56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], 75])
test_function([[56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], 0])

# target None
print('-----------------target None-----------------------')
test_function([[82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], None])

# empty array
print('------------------empty array----------------------')
test_function([[], 12])

# array with one or two elements
print('------------------array with one or two elements----------------------')
test_function([[12], 12])
test_function([[12, 13], 12])

# array not rotated
print('------------------array not rotated----------------------')
test_function([[56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], 75])




