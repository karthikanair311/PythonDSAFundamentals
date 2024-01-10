"""
Python Script for Finding and Printing the ith Node in a Singly Linked List

This script defines functions to build a singly linked list from input and find and print the data of the node at a specific position ('i') in the list.
It demonstrates the use of iterative traversal in Python for linked lists and includes an example of how to use the functions.

Functions:
    ithNode(head, i): Find and return the node at the 'i-th' position in the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def ithNode(head, i):
    """
    Find and return the node at the 'i-th' position in the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.
    - i (int): The position of the node to find.

    Returns:
    Node: The node at the 'i-th' position, or None if the position is invalid.

    Example:
    - Given a linked list with head 'head' and a position 'i', ithNode(head, i) will return the node at the 'i-th' position.
    """
    count = 0
    current = head
    while current is not None and count < i:
        current = current.next
        count += 1
    return current

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
    # Array: [1, 2, 3, 4, 5, -1], Position i: 2
    # Expected Output: 3
    arr_example1 = [1, 2, 3, 4, 5, -1]
    i_example1 = 2
    l_example1 = ll(arr_example1[:-1])
    node_example1 = ithNode(l_example1, i_example1)
    assert node_example1.data == 3, "Example 1 failed"

    # Example 2:
    # Array: [10, 20, 30, 40, -1], Position i: 0
    # Expected Output: 10
    arr_example2 = [10, 20, 30, 40, -1]
    i_example2 = 0
    l_example2 = ll(arr_example2[:-1])
    node_example2 = ithNode(l_example2, i_example2)
    assert node_example2.data == 10, "Example 2 failed"

    # Example 3:
    # Array: [7, 14, 21, -1], Position i: 3
    # Expected Output: No output or a message indicating an invalid position
    arr_example3 = [7, 14, 21, -1]
    i_example3 = 3
    l_example3 = ll(arr_example3[:-1])
    node_example3 = ithNode(l_example3, i_example3)
    assert node_example3 is None, "Example 3 failed"
