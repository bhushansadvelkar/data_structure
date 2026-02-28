"""
Insert and Delete Operations on Linked List

Difficulty: Easy / Medium
Topics: Linked List


Problem:
--------
Implement insert and delete operations on a singly linked list. All operations
take the head of the list and return the (possibly new) head. Indices are
0-based. Invalid index: return head unchanged (or handle as needed).

Operations:
-----------
- insert_at_head(head, val): Insert node with value val at the beginning.
  Return the new head.
- insert_at_tail(head, val): Insert node with value val at the end.
  Return head (if list was empty, new head is the new node).
- insert_at_index(head, index, val): Insert node before the index-th node.
  If index == length, append. If index > length, do nothing. Return head.
- delete_at_head(head): Remove the first node. Return new head (None if list
  becomes empty).
- delete_at_tail(head): Remove the last node. Return head (None if list
  becomes empty).
- delete_at_index(head, index): Remove the index-th node. If index invalid,
  return head unchanged. Return head.

Examples:
---------
insert_at_head(None, 1)     -> 1
insert_at_tail(1->2, 3)     -> 1->2->3
insert_at_index(1->3, 1, 2) -> 1->2->3
delete_at_head(1->2->3)     -> 2->3
delete_at_tail(1->2->3)     -> 1->2
delete_at_index(1->2->3, 1) -> 1->3

Constraints:
------------
- 0 <= index <= length of list
- -10^5 <= val <= 10^5

How I solved it:
---------------
- insert_at_head: Create node, set node.next = head, return node.
- insert_at_tail: If empty return new node. Else traverse to last node, append.
- insert_at_index: Index 0 → insert_at_head. Else traverse to (index-1)-th,
  insert new node between curr and curr.next.
- delete_at_head: Return head.next (or None).
- delete_at_tail: Traverse to second-last, set curr.next = None.
- delete_at_index: Index 0 → delete_at_head. Else traverse to (index-1)-th,
  set curr.next = curr.next.next.

Time Complexity: O(1) for insert/delete at head; O(n) for tail or at index.
Space Complexity: O(1) per operation.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_list(arr):
    """Build linked list from list."""
    if not arr:
        return None
    dummy = ListNode(0)
    p = dummy
    for x in arr:
        p.next = ListNode(x)
        p = p.next
    return dummy.next


def list_to_array(head):
    """Convert linked list to list for comparison."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def insert_at_head(head, val):
    """
    Insert a node with value val at the beginning. Return the new head.

    How: Create new node with val, set new_node.next = head, return new_node.
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    node = ListNode(val)
    node.next = head 
    return node 


def insert_at_tail(head, val):
    """
    Insert a node with value val at the end. Return head (or new head if was empty).

    How: If head is None, return ListNode(val). Else traverse to the last node,
    set last.next = ListNode(val). Return head.
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    curr = head
    node = ListNode(val)

    if not head:
        return node 

    if curr.next is None:
        curr.next = node
        return head

    while curr.next:
        curr = curr.next 

    curr.next = node
    return head


def insert_at_index(head, index, val):
    """
    Insert a node with value val before the index-th node. If index == length,
    append. If index > length, return head unchanged. Return head (or new head
    if insert at 0).

    How: If index == 0, same as insert_at_head. Else traverse to the (index-1)-th
    node, set new_node.next = curr.next, curr.next = new_node.
    :type head: ListNode
    :type index: int
    :type val: int
    :rtype: ListNode
    """
    if index == 0:
        return insert_at_head(head, val)

    if not head:
        return None

    node = ListNode(val)
    curr = head
    for _ in range(index - 1):
        if curr is None:
            return head
        curr = curr.next
    if curr is None:
        return head
    node.next = curr.next
    curr.next = node
    return head


def delete_at_head(head):
    """
    Remove the first node. Return new head (None if list had one node).

    How: If head is None, return None. Return head.next.
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return head

    temp = head 
    head = head.next
    return head 


def delete_at_tail(head):
    """
    Remove the last node. Return head (None if list had one node).

    How: If head is None or head.next is None, return None. Traverse to the
    second-last node, set curr.next = None. Return head.
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or head.next is None:
        return None

    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None

    return head


def delete_at_index(head, index):
    """
    Remove the index-th node. If index invalid, return head unchanged.
    Return head (or new head if index was 0).

    How: If index == 0, return head.next. Else traverse to the (index-1)-th
    node, set curr.next = curr.next.next (if curr.next exists).
    :type head: ListNode
    :type index: int
    :rtype: ListNode
    """
    if not head:
        return None
        
    curr = head
    if index == 0:
        return delete_at_head(head)
    else:
        for _ in range(index - 1):
            if curr is None:
                return head
            curr = curr.next
        if curr is None or curr.next is None:
            return head
        curr.next = curr.next.next

    return head 


if __name__ == "__main__":
    def to_list(head):
        return list_to_array(head) if head is not None else []

    # insert_at_head
    run_test(to_list(insert_at_head(None, 1)), [1], "insert_at_head(None, 1)")
    run_test(to_list(insert_at_head(array_to_list([2, 3]), 1)), [1, 2, 3], "insert_at_head(2->3, 1)")
    run_test(to_list(insert_at_head(array_to_list([5]), 0)), [0, 5], "insert_at_head(single 5, 0)")
    run_test(to_list(insert_at_head(array_to_list([10, 20]), 5)), [5, 10, 20], "insert_at_head(10->20, 5)")
    run_test(to_list(insert_at_head(array_to_list([1, 2, 3]), 0)), [0, 1, 2, 3], "insert_at_head(1->2->3, 0)")
    run_test(to_list(insert_at_head(array_to_list([1]), 2)), [2, 1], "insert_at_head(single 1, 2)")

    # insert_at_tail
    run_test(to_list(insert_at_tail(None, 1)), [1], "insert_at_tail(None, 1)")
    run_test(to_list(insert_at_tail(array_to_list([1, 2]), 3)), [1, 2, 3], "insert_at_tail(1->2, 3)")
    run_test(to_list(insert_at_tail(array_to_list([5]), 10)), [5, 10], "insert_at_tail(single 5, 10)")
    run_test(to_list(insert_at_tail(array_to_list([1, 2, 3]), 4)), [1, 2, 3, 4], "insert_at_tail(1->2->3, 4)")
    run_test(to_list(insert_at_tail(array_to_list([10]), 0)), [10, 0], "insert_at_tail(single 10, 0)")
    run_test(to_list(insert_at_tail(array_to_list([1]), 2)), [1, 2], "insert_at_tail(single 1, 2)")

    # insert_at_index
    run_test(to_list(insert_at_index(array_to_list([1, 3]), 1, 2)), [1, 2, 3], "insert_at_index(1->3, 1, 2)")
    run_test(to_list(insert_at_index(array_to_list([2, 3]), 0, 1)), [1, 2, 3], "insert_at_index(2->3, 0, 1)")
    run_test(to_list(insert_at_index(array_to_list([1, 2]), 2, 3)), [1, 2, 3], "insert_at_index(1->2, 2 append)")
    run_test(to_list(insert_at_index(array_to_list([1]), 1, 2)), [1, 2], "insert_at_index(single 1, 1, 2)")
    run_test(to_list(insert_at_index(array_to_list([1]), 0, 0)), [0, 1], "insert_at_index(single 1, 0, 0)")
    run_test(to_list(insert_at_index(array_to_list([1, 2, 3]), 0, 0)), [0, 1, 2, 3], "insert_at_index(1->2->3, 0, 0)")
    run_test(to_list(insert_at_index(array_to_list([1, 2, 3]), 3, 4)), [1, 2, 3, 4], "insert_at_index(1->2->3, 3 append)")
    run_test(to_list(insert_at_index(None, 0, 1)), [1], "insert_at_index(None, 0, 1)")

    # delete_at_head
    run_test(to_list(delete_at_head(array_to_list([1, 2, 3]))), [2, 3], "delete_at_head(1->2->3)")
    run_test(to_list(delete_at_head(array_to_list([1]))), [], "delete_at_head(single)")

    # delete_at_tail
    run_test(to_list(delete_at_tail(array_to_list([1, 2, 3]))), [1, 2], "delete_at_tail(1->2->3)")
    run_test(to_list(delete_at_tail(array_to_list([1]))), [], "delete_at_tail(single)")

    # delete_at_index
    run_test(to_list(delete_at_index(array_to_list([1, 2, 3]), 1)), [1, 3], "delete_at_index(1->2->3, 1)")
    run_test(to_list(delete_at_index(array_to_list([1, 2, 3]), 0)), [2, 3], "delete_at_index(1->2->3, 0)")
    run_test(to_list(delete_at_index(array_to_list([1, 2, 3]), 2)), [1, 2], "delete_at_index(1->2->3, 2) last")
    run_test(to_list(delete_at_index(array_to_list([1]), 0)), [], "delete_at_index(single, 0)")
    run_test(to_list(delete_at_index(array_to_list([1, 2]), 1)), [1], "delete_at_index(1->2, 1)")
    run_test(to_list(delete_at_index(array_to_list([1, 2, 3]), 3)), [1, 2, 3], "delete_at_index(1->2->3, 3) invalid")
    run_test(to_list(delete_at_index(array_to_list([1, 2, 3]), 5)), [1, 2, 3], "delete_at_index(1->2->3, 5) invalid")
    run_test(to_list(delete_at_index(None, 0)), [], "delete_at_index(None, 0)")
