"""
Python Script for Finding the Length of a Singly Linked List

This script defines functions to build a singly linked list from input and calculate its length using an iterative method.
It demonstrates the use of iterative traversal in Python for linked lists and includes an example of how to use the functions.

Functions:
    findlength(head): Calculate the length of the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findlength(head):
    """
    Calculate the length of the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.

    Returns:
    int: The length of the linked list.

    Example:
    - Given a linked list with head 'head', findlength(head) will return the length of the list.
    """
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count

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
    # Array: [1, 2, 3, 4, 5, -1]
    # Expected Output: Length of the linked list: 5
    arr_example1 = [1, 2, 3, 4, 5, -1]
    l_example1 = ll(arr_example1[:-1])
    length_example1 = findlength(l_example1)
    assert length_example1 == 5, "Example 1 failed"

    # Example 2:
    # Array: [10, 20, 30, 40, -1]
    # Expected Output: Length of the linked list: 4
    arr_example2 = [10, 20, 30, 40, -1]
    l_example2 = ll(arr_example2[:-1])
    length_example2 = findlength(l_example2)
    assert length_example2 == 4, "Example 2 failed"

    # Example 3:
    # Array: [-1]
    # Expected Output: Length of the linked list: 0
    arr_example3 = [-1]
    l_example3 = ll(arr_example3[:-1])
    length_example3 = findlength(l_example3)
    assert length_example3 == 0, "Example 3 failed"
