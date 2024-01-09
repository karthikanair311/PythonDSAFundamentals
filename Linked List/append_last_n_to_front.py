"""
Python Script for Appending Last 'N' Nodes to Front in a Singly Linked List

This script defines functions to build a singly linked list from input and append the last 'N' nodes to the front of the list.
It demonstrates the use of iterative list manipulation in Python for linked lists and includes an example of how to use the functions.

Functions:
    append_LinkedList(head, n): Append the last 'n' nodes to the front of the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    """
    Calculate the length of the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.

    Returns:
    int: The length of the linked list.
    """
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def append_LinkedList(head, n):
    """
    Append the last 'n' nodes to the front of the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.
    - n (int): The number of nodes to move from the end to the front.

    Returns:
    Node: The new head of the modified linked list.

    Example:
    - Given a linked list with head 'head' and a number 'n', append_LinkedList(head, n) rearranges the list and returns the new head.
    """
    if not head or not head.next or n <= 0:
        return head

    l = length(head)
    if n >= l:
        return head

    count = 0
    current = head
    while count < l - n - 1:
        current = current.next
        count += 1
    
    new_head = current.next
    current.next = None
    temp = new_head
    while temp.next:
        temp = temp.next
    temp.next = head

    return new_head

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
    # Array: [1, 2, 3, 4, 5, -1], Number n: 2
    # Expected Output: Modified linked list: 4 5 1 2 3
    arr_example1 = [1, 2, 3, 4, 5, -1]
    n_example1 = 2
    l_example1 = ll(arr_example1[:-1])
    l_example1 = append_LinkedList(l_example1, n_example1)
    # Verifying the output
    expected_output_example1 = [4, 5, 1, 2, 3]
    current_example1 = l_example1
    for expected_data in expected_output_example1:
        assert current_example1.data == expected_data, "Example 1 failed"
        current_example1 = current_example1.next

    # Example 2:
    # Array: [10, 20, 30, 40, -1], Number n: 3
    # Expected Output: Modified linked list: 20 30 40 10
    arr_example2 = [10, 20, 30, 40, -1]
    n_example2 = 3
    l_example2 = ll(arr_example2[:-1])
    l_example2 = append_LinkedList(l_example2, n_example2)
    # Verifying the output
    expected_output_example2 = [20, 30, 40, 10]
    current_example2 = l_example2
    for expected_data in expected_output_example2:
        assert current_example2.data == expected_data, "Example 2 failed"
        current_example2 = current_example2.next

    # Example 3:
    # Array: [7, 14, 21, -1], Number n: 0
    # Expected Output: Modified linked list: 7 14 21
    arr_example3 = [7, 14, 21, -1]
    n_example3 = 0
    l_example3 = ll(arr_example3[:-1])
    l_example3 = append_LinkedList(l_example3, n_example3)
    # Verifying the output
    expected_output_example3 = [7, 14, 21]
    current_example3 = l_example3
    for expected_data in expected_output_example3:
        assert current_example3.data == expected_data, "Example 3 failed"
        current_example3 = current_example3.next
