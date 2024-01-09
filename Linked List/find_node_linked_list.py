"""
Python Script for Finding a Node in a Singly Linked List

This script defines functions to build a singly linked list from input and find the index of a specified number in the list.
It demonstrates the use of recursion in Python for linked list manipulation and includes an example of how to use the functions.

Functions:
    findNode(head, number, index): Find and return the index of the specified number in the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findNode(head, number, index):
    """
    Find and return the index of the specified number in the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.
    - number (int): The number to find in the linked list.
    - index (int): The starting index for the search, initially set to 0.

    Returns:
    int: The index of the number if found, -1 otherwise.

    Example:
    - Given a linked list with head 'head' and a number 'number', findNode(head, number, 0) will return the index of the number.
    """
    if head is None:
        return -1
    if head.data == number:
        return index
    return findNode(head.next, number, index + 1)

def ll(arr):
    """
    Build a singly linked list from the given array.

    Parameters:
    - arr (list of int): The array containing the elements of the linked list.

    Returns:
    Node: The head node of the constructed linked list.
    """
    if not arr:
        return None

    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Example Usage:
if __name__ == "__main__":
    # Example 1:
    # Array: [1, 2, 3, 4, 5, -1], Number to find: 3
    # Expected Output: Index of the number 3 in the linked list: 2
    arr_example1 = [1, 2, 3, 4, 5, -1]
    number_to_find_example1 = 3
    l_example1 = ll(arr_example1[:-1])
    index_example1 = findNode(l_example1, number_to_find_example1, 0)
    assert index_example1 == 2, "Example 1 failed"

    # Example 2:
    # Array: [10, 20, 30, 40, -1], Number to find: 20
    # Expected Output: Index of the number 20 in the linked list: 1
    arr_example2 = [10, 20, 30, 40, -1]
    number_to_find_example2 = 20
    l_example2 = ll(arr_example2[:-1])
    index_example2 = findNode(l_example2, number_to_find_example2, 0)
    assert index_example2 == 1, "Example 2 failed"

    # Example 3:
    # Array: [7, 14, 21, -1], Number to find: 15
    # Expected Output: Index of the number 15 in the linked list: -1
    arr_example3 = [7, 14, 21, -1]
    number_to_find_example3 = 15
    l_example3 = ll(arr_example3[:-1])
    index_example3 = findNode(l_example3, number_to_find_example3, 0)
    assert index_example3 == -1, "Example 3 failed"
