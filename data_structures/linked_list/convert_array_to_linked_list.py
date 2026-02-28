"""
Convert Array to Linked List

Difficulty: Easy
Topics: Linked List


Problem:
--------
Given an array of integers (or values), convert it into a singly linked list.
Return the head of the linked list. The order of elements in the array should
be preserved in the linked list (first element becomes head, then next, etc.).

If the array is empty, return None.

Examples:
---------
Example 1:
    Input: arr = [1, 2, 3]
    Output: Linked list 1 -> 2 -> 3 (head points to 1)

Example 2:
    Input: arr = []
    Output: None

Example 3:
    Input: arr = [10]
    Output: Linked list with single node 10

Constraints:
------------
- 0 <= len(arr) <= 10^4
- -10^5 <= arr[i] <= 10^5

How I solved it:
----------------
Use a dummy head: create a dummy node, traverse the array, create a new node
for each value and link it to the tail. Return dummy.next so the first real
node is the head. Empty array returns None.

Time Complexity: O(n)
    One pass over the array; create n nodes.

Space Complexity: O(n)
    n nodes for the linked list (output). O(1) extra besides the result.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_array(head):
    """Convert linked list to list for comparison."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def traverse_linked_list(head):
    """
    Traverse a singly linked list from head to tail.

    How to traverse:
        - Start at head. Use a pointer (e.g. current) that moves node by node.
        - Loop while current is not None: read/use current.val, then move
          current = current.next.
        - When current becomes None, you've reached the end (past the last node).

    :type head: ListNode
    :rtype: List[int]
    """
    current = head 
    result = []

    while current:
        result.append(current.val)
        current = current.next
    
    return result


def length_of_linked_list(head):
    """
    Return the number of nodes in the linked list (length / size).

    How to calculate length:
        - Traverse the list from head to tail (same pattern as traverse:
          current = head, then while current: ... current = current.next).
        - Count each node you visit. When current becomes None, return the count.
        - Empty list (head is None) has length 0.

    :type head: ListNode
    :rtype: int
    """
    current = head 
    length = 0 

    while current:
        current = current.next
        length += 1
    
    return length


def search_in_linked_list(head, target):
    """
    Return True if target exists in the linked list, else False.

    How to search:
        - Traverse the list from head (current = head, while current: ...).
        - At each node, check if current.val == target; if yes, return True.
        - If you reach the end (current becomes None) without finding target,
          return False.
        - Empty list (head is None): return False.

    :type head: ListNode
    :type target: int
    :rtype: bool
    """
    current = head 
    while current:
        if current.val == target:
            return True
        current = current.next

    return False


def array_to_linked_list(arr):
    """
    Convert array to singly linked list. Return head; empty array returns None.

    :type arr: List[int]
    :rtype: ListNode
    """
    if not arr:
        return None 

    head = ListNode(arr[0])
    tail = head 

    for i in range(1, len(arr)):
        tail.next = ListNode(arr[i])
        tail = tail.next
    
    return head

if __name__ == "__main__":
    def head_to_list(head):
        return list_to_array(head) if head is not None else []

    run_test(head_to_list(array_to_linked_list([1, 2, 3])), [1, 2, 3], "arr=[1,2,3]")
    run_test(head_to_list(array_to_linked_list([])), [], "arr=[]")
    run_test(head_to_list(array_to_linked_list([10])), [10], "arr=[10]")
    run_test(head_to_list(array_to_linked_list([5, 0, -1, 2])), [5, 0, -1, 2], "arr=[5,0,-1,2]")

    # Traverse: build list then traverse it
    head = array_to_linked_list([1, 2, 3])
    run_test(traverse_linked_list(head), [1, 2, 3], "traverse 1->2->3")
    run_test(traverse_linked_list(None), [], "traverse empty (None)")

    # Length of linked list
    run_test(length_of_linked_list(array_to_linked_list([1, 2, 3])), 3, "length of 1->2->3")
    run_test(length_of_linked_list(None), 0, "length of empty (None)")
    run_test(length_of_linked_list(array_to_linked_list([10])), 1, "length of single node")

    # Search in linked list
    head = array_to_linked_list([1, 2, 3])
    run_test(search_in_linked_list(head, 2), True, "search 2 in 1->2->3")
    run_test(search_in_linked_list(head, 5), False, "search 5 in 1->2->3")
    run_test(search_in_linked_list(None, 1), False, "search in empty list")
    run_test(search_in_linked_list(array_to_linked_list([10]), 10), True, "search 10 in single node")
