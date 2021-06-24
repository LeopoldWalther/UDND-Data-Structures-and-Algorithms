# Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
# You're not allowed to use any sorting function that Python provides.
# Note: O(n) does not necessarily mean single-traversal.
# If you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None:
        return -1

    low = 0
    mid = 0
    high = len(input_list)-1

    while mid <= high:
        if input_list[mid] == 0:
            input_list[mid], input_list[low] = input_list[low], input_list[mid]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        elif input_list[mid] == 2:
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1
        else:
            return None

    return input_list



def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


print('--------------------given test functions--------------------')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

print('--------------------only one kind of digit--------------------')
test_function([0, 0, 0, 0, 0, 0])
test_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
test_function([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

print('--------------------few elements--------------------')
test_function([1, 0])
test_function([1])

print('--------------------not allowed digit--------------------')
test_function([1, 0, 3, 5, 7])
test_function([8])

print('--------------------empty list--------------------')
test_function([])


