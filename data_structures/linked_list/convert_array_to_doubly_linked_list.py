"""
Convert Array to Doubly Linked List

Difficulty: Easy
Topics: Linked List

Problem:
--------
Given an array of integers (or values), convert it into a doubly linked list.
Return the head of the list. Each node has val, next, and prev. The order of
elements in the array is preserved (first element is head, last is tail).

If the array is empty, return None.

Examples:
---------
Example 1:
    Input: arr = [1, 2, 3]
    Output: Doubly linked list 1 <-> 2 <-> 3 (head=1, tail=3)

Example 2:
    Input: arr = []
    Output: None

Example 3:
    Input: arr = [10]
    Output: Single node 10 (prev=None, next=None)

Constraints:
------------
- 0 <= len(arr) <= 10^4
- -10^5 <= arr[i] <= 10^5

How I solved it:
----------------
(TODO: use head and tail; link next and prev; empty array returns None.)

Time Complexity: O(n)
Space Complexity: O(n) for n nodes.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class DoublyListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def list_to_array_forward(head):
    """Convert doubly linked list to list from head to tail (using next)."""
    pass


def list_to_array_backward(tail):
    """Convert doubly linked list to list from tail to head (using prev)."""
    pass


def get_tail(head):
    """Return the last node of the list (tail)."""
    pass


def traverse_forward(head):
    """
    Traverse the doubly linked list from head to tail using next.

    :type head: DoublyListNode
    :rtype: List[int]
    """
    if head is None:
        return []

    result = []

    curr = head 

    while curr:
        result.append(curr.val)
        curr = curr.next

    return result


def traverse_backward(tail):
    """
    Traverse the doubly linked list from tail to head using prev.

    :type tail: DoublyListNode
    :rtype: List[int]
    """
    pass


def length_of_doubly_linked_list(head):
    """Return the number of nodes. Empty list returns 0."""
    pass


def search_in_doubly_linked_list(head, target):
    """Return True if target exists in the list, else False."""
    pass


def array_to_doubly_linked_list(arr):
    """
    Convert array to doubly linked list. Return head; empty array returns None.
    Each node's prev points to the previous node; head.prev is None; tail.next is None.

    :type arr: List[int]
    :rtype: DoublyListNode
    """
    if not arr:
        return None 

    head = DoublyListNode(arr[0])
    tail = head 

    for i in range(1, len(arr)):
        node = DoublyListNode(arr[i])
        tail.next = node 
        tail.prev = tail 
        tail = node 

    return head

if __name__ == "__main__":
    def head_to_list(head):
        return list_to_array_forward(head) if head is not None else []

    # # --- array_to_doubly_linked_list ---
    # run_test(head_to_list(array_to_doubly_linked_list([1, 2, 3])), [1, 2, 3], "arr=[1,2,3]")
    # run_test(head_to_list(array_to_doubly_linked_list([])), [], "arr=[]")
    # run_test(head_to_list(array_to_doubly_linked_list([10])), [10], "arr=[10]")
    # run_test(
    #     head_to_list(array_to_doubly_linked_list([5, 0, -1, 2])),
    #     [5, 0, -1, 2],
    #     "arr=[5,0,-1,2]",
    # )
    # run_test(head_to_list(array_to_doubly_linked_list([7, 7, 7])), [7, 7, 7], "arr=[7,7,7]")
    # run_test(
    #     head_to_list(array_to_doubly_linked_list([-100, 0, 100])),
    #     [-100, 0, 100],
    #     "arr=[-100,0,100]",
    # )
    # run_test(
    #     head_to_list(array_to_doubly_linked_list([1, 2, 3, 4, 5])),
    #     [1, 2, 3, 4, 5],
    #     "arr=[1,2,3,4,5]",
    # )

    # --- traverse_forward ---
    head = array_to_doubly_linked_list([1, 2, 3])
    run_test(traverse_forward(head), [1, 2, 3], "traverse forward 1<->2<->3")
    run_test(traverse_forward(None), [], "traverse forward empty")
    head = array_to_doubly_linked_list([1])
    run_test(traverse_forward(head), [1], "traverse forward single node")
    head = array_to_doubly_linked_list([1, 2, 3, 4])
    run_test(traverse_forward(head), [1, 2, 3, 4], "traverse forward 1<->2<->3<->4")

    # # --- traverse_backward (from tail) ---
    # head = array_to_doubly_linked_list([1, 2, 3])
    # tail = get_tail(head)
    # run_test(traverse_backward(tail), [3, 2, 1], "traverse backward from tail")
    # run_test(traverse_backward(None), [], "traverse backward empty")
    # head = array_to_doubly_linked_list([1])
    # tail = get_tail(head)
    # run_test(traverse_backward(tail), [1], "traverse backward single node")
    # head = array_to_doubly_linked_list([4, 3, 2, 1])
    # tail = get_tail(head)
    # run_test(traverse_backward(tail), [1, 2, 3, 4], "traverse backward 4<->3<->2<->1")

    # # --- get_tail ---
    # head = array_to_doubly_linked_list([1, 2, 3])
    # tail = get_tail(head)
    # run_test(tail.val if tail else None, 3, "get_tail([1,2,3]) val")
    # run_test(get_tail(None), None, "get_tail(None)")
    # head = array_to_doubly_linked_list([99])
    # tail = get_tail(head)
    # run_test(tail.val if tail else None, 99, "get_tail single node")

    # # --- list_to_array_backward ---
    # head = array_to_doubly_linked_list([1, 2, 3])
    # tail = get_tail(head)
    # run_test(list_to_array_backward(tail), [3, 2, 1], "list_to_array_backward")
    # run_test(list_to_array_backward(None), [], "list_to_array_backward None")

    # # --- length_of_doubly_linked_list ---
    # run_test(
    #     length_of_doubly_linked_list(array_to_doubly_linked_list([1, 2, 3])),
    #     3,
    #     "length of 1<->2<->3",
    # )
    # run_test(length_of_doubly_linked_list(None), 0, "length of empty")
    # run_test(
    #     length_of_doubly_linked_list(array_to_doubly_linked_list([10])),
    #     1,
    #     "length of single node",
    # )
    # run_test(
    #     length_of_doubly_linked_list(array_to_doubly_linked_list([1, 2, 3, 4, 5])),
    #     5,
    #     "length of 5 nodes",
    # )
    # run_test(
    #     length_of_doubly_linked_list(array_to_doubly_linked_list([])),
    #     0,
    #     "length of empty (from [])",
    # )

    # # --- search_in_doubly_linked_list ---
    # head = array_to_doubly_linked_list([1, 2, 3])
    # run_test(search_in_doubly_linked_list(head, 2), True, "search 2 in list")
    # run_test(search_in_doubly_linked_list(head, 5), False, "search 5 in list")
    # run_test(search_in_doubly_linked_list(None, 1), False, "search in empty list")
    # run_test(
    #     search_in_doubly_linked_list(array_to_doubly_linked_list([10]), 10),
    #     True,
    #     "search 10 in single node",
    # )
    # head = array_to_doubly_linked_list([1, 2, 3])
    # run_test(search_in_doubly_linked_list(head, 1), True, "search head val")
    # run_test(search_in_doubly_linked_list(head, 3), True, "search tail val")
    # run_test(search_in_doubly_linked_list(head, 0), False, "search missing")
