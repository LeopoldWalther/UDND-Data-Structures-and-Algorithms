# Max and Min in a Unsorted Array
# In this problem, we will look for smallest and largest integer from a list of unsorted integers.
# The code should run in O(n) time.
# Do not use Python's inbuilt functions to find min and max.
# Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?

import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    min_element = ints[0]
    max_element = ints[len(ints) - 1]

    for element in ints:
        if element < min_element:
            min_element = element
        if element > max_element:
            max_element = element

    return min_element, max_element


print('--------------------given test functions--------------------')
test_list_1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(test_list_1)
print('Pass' if ((0, 9) == get_min_max(test_list_1)) else 'Fail')

print('--------------------long input list--------------------')
test_list_2 = [i for i in range(0, 10000)]  # a list containing 0 - 9
random.shuffle(test_list_2)
print('Pass' if ((0, 9999) == get_min_max(test_list_2)) else 'Fail')

print('--------------------empty input list--------------------')
test_list_3 = []
print('Pass' if get_min_max(test_list_3) is None else 'Fail')

print('--------------------empty input list--------------------')
test_list_4 = [0] * 100
print('Pass' if get_min_max(test_list_4) == (0, 0) else 'Fail')