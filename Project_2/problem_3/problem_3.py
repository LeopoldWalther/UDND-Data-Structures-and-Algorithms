# Rearrange Array Elements so as to form two numbers such that their sum is maximum.
# Return these two numbers.
# You can assume that all array elements are in the range [0, 9].
# The number of digits in both the numbers cannot differ by more than 1.
# You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
# for e.g. [1, 2, 3, 4, 5] the expected answer would be [531, 42]. Another expected answer can be [542, 31].
# In scenarios such as these when there are more than one possible answers, return any one.

# go through input list and alternately add element to both output numbers

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or input_list == []:
        return -1, -1

    for element in input_list:
        if type(element) is not int:
            return -1, -1

    number_one = []
    number_two = []
    counter = 0

    sorted_input_list = mergesort(input_list)  # Time: O(n*log(n)), Space: O(n)
    for element in sorted_input_list:
        if counter % 2 == 0:
            number_one.append(str(element))
        else:
            number_two.append(str(element))
        counter += 1

    number_one = "".join(number_one)
    number_two = "".join(number_two)

    return int(number_one), int(number_two)


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
        if left_sub_array[left_index] < right_sub_array[right_index]:
            merged.append(right_sub_array[right_index])
            right_index += 1
        else:
            merged.append(left_sub_array[left_index])
            left_index += 1

    # add what is left in one of the arrays
    merged += left_sub_array[left_index:]
    merged += right_sub_array[right_index:]

    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


print('--------------------given test functions--------------------')
test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case_1)

print('--------------------repeating digits--------------------')
test_case_2 = [[0, 1, 2, 3, 4, 5, 6, 9, 9, 9, 9, 9, 9, 3, 4, 5, 6], [999654320, 99965431]]
test_function(test_case_2)

print('--------------------only one int, but repeated--------------------')
test_case_3 = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [33333, 33333]]
test_function(test_case_3)

print('--------------------character in list--------------------')
test_case_4 = [[4, 6, 'a', 5, 9, 8], [-1, -1]]
test_function(test_case_4)

print('--------------------empty list--------------------')
test_case_5 = [[], [-1, -1]]
test_function(test_case_5)

print('--------------------None for list--------------------')
test_case_5 = [None, [-1, -1]]
test_function(test_case_5)
