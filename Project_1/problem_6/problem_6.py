import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        head = self.head
        out_string = ""
        while head:
            out_string += str(head.value) + " -> "
            head = head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(linked_list_1, linked_list_2):
    """The union of two sets A and B is the set of elements which are in A, in B, or in both A and B"""
    cloned_linked_list_1 = clone_linked_list(linked_list_1)
    cloned_linked_list_2 = clone_linked_list(linked_list_2)

    node = cloned_linked_list_1.head
    if node is None:
        return cloned_linked_list_2
    else:
        while node.next:
            node = node.next
        node.next = cloned_linked_list_2.head

    return cloned_linked_list_1


def clone_linked_list(linked_list):
    cloned_list = LinkedList()
    node = linked_list.head
    while node:
        new_node = Node(node.value)
        cloned_list.append(new_node)
        node = node.next
    return cloned_list


def intersection(linked_list_1, linked_list_2):

    intersection_dictionary = dict()
    intersection_dictionary = create_dictionary_from_linked_list(linked_list_1, intersection_dictionary, True)
    intersection_dictionary = create_dictionary_from_linked_list(linked_list_2, intersection_dictionary, False)
    union_linked_list = LinkedList()
    for key, value in intersection_dictionary.items():
        if value >= 2:
            union_linked_list.append(key)
    return union_linked_list


def create_dictionary_from_linked_list(linked_list, dictionary, first_list):
    node = linked_list.head
    while node is not None:
        if node.value not in dictionary and first_list:
            dictionary[node.value] = 1
        elif node.value in dictionary and not first_list:
            dictionary[node.value] += 1
        node = node.next
    return dictionary


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 ->
print(intersection(linked_list_1, linked_list_2))
# 4 -> 6 -> 21

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 ->
print(intersection(linked_list_3, linked_list_4))
# no output


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# no output
print(intersection(linked_list_5, linked_list_6))
# no output


# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 49, 49, 49, 49]
element_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 49, 49, 49, 49]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 ->
# 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32 -> 33 -> 34 -> 35 -> 36 -> 37 -> 38 -> 39 -> 40 ->
# 41 -> 42 -> 43 -> 44 -> 45 -> 46 -> 47 -> 48 -> 49 -> 49 -> 49 -> 49 -> 49 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 ->
# 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 ->
# 29 -> 30 -> 31 -> 32 -> 33 -> 34 -> 35 -> 36 -> 37 -> 38 -> 39 -> 40 -> 41 -> 42 -> 43 -> 44 -> 45 -> 46 -> 47 ->
# 48 -> 49 -> 49 -> 49 -> 49 -> 49 ->

print(intersection(linked_list_7, linked_list_8))
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 ->
# 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32 -> 33 -> 34 -> 35 -> 36 -> 37 -> 38 -> 39 -> 40 ->
# 41 -> 42 -> 43 -> 44 -> 45 -> 46 -> 47 -> 48 -> 49 ->


# Test case 5

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [-1, -2, -2.1]
element_2 = [-2.1]

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))
# -1 -> -2 -> -2.1 -> -2.1 ->
print(intersection(linked_list_9, linked_list_10))
# -2.1 ->


# Test case 6

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [-1, -2, -2.1]
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))
# -1 -> -2 -> -2.1 -> -2.1 ->
print(intersection(linked_list_9, linked_list_10))
# no output

