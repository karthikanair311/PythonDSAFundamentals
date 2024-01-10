"""
Python Script for Deleting a Node from a Singly Linked List

This script defines functions to build a singly linked list from input and delete a node from a specific position in the list.
It demonstrates the use of recursion in Python for linked list manipulation and includes an example of how to use the functions.

Functions:
    deleteRec(head, i): Delete the node at the 'i-th' position in the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteRec(head, i):
    """
    Delete the node at the 'i-th' position in the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.
    - i (int): The position of the node to be deleted.

    Returns:
    Node: The head of the modified linked list.

    Example:
    - Given a linked list with head 'head' and a position 'i', deleteRec(head, i) will delete the node at the 'i-th' position.
    """
    if i < 0:
        return head
    if head is None:
        return None
    if i == 0:
        return head.next
    head.next = deleteRec(head.next, i - 1)
    return head

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
    # Array: [1, 2, 3, 4, 5, -1], Position i to delete: 2
    # Expected Output: Modified linked list: 1 2 4 5
    arr_example1 = [1, 2, 3, 4, 5, -1]
    i_example1 = 2
    l_example1 = ll(arr_example1[:-1])
    l_example1 = deleteRec(l_example1, i_example1)
    # Verifying the output
    expected_output_example1 = [1, 2, 4, 5]
    current_example1 = l_example1
    for expected_data in expected_output_example1:
        assert current_example1.data == expected_data, "Example 1 failed"
        current_example1 = current_example1.next

    # Example 2:
    # Array: [10, 20, 30, 40, -1], Position i to delete: 0
    # Expected Output: Modified linked list: 20 30 40
    arr_example2 = [10, 20, 30, 40, -1]
    i_example2 = 0
    l_example2 = ll(arr_example2[:-1])
    l_example2 = deleteRec(l_example2, i_example2)
    # Verifying the output
    expected_output_example2 = [20, 30, 40]
    current_example2 = l_example2
    for expected_data in expected_output_example2:
        assert current_example2.data == expected_data, "Example 2 failed"
        current_example2 = current_example2.next

    # Example 3:
    # Array: [7, 14, 21, -1], Position i to delete: 3
    # Expected Output: Modified linked list: 7 14 21
    arr_example3 = [7, 14, 21, -1]
    i_example3 = 3
    l_example3 = ll(arr_example3[:-1])
    l_example3 = deleteRec(l_example3, i_example3)
    # Verifying the output
    expected_output_example3 = [7, 14, 21]
    current_example3 = l_example3
    for expected_data in expected_output_example3:
        assert current_example3.data == expected_data, "Example 3 failed"
        current_example3 = current_example3.next
