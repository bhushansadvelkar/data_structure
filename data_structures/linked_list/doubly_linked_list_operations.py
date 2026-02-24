"""
Doubly Linked List Operations - Practice Add & Delete

Difficulty: Easy
Topics: Linked List

Problem:
--------
Practice adding and deleting nodes in a doubly linked list.
Implement operations: add at head, add at tail, add at index;
delete at head, delete at tail, delete by value, delete at index.

Node structure: val, next, prev
- head.prev is None
- tail.next is None

How I solved it:
----------------
Add: create node, link prev/next; handle empty list and index 0 (head). Delete:
unlink node (update prev.next and next.prev); handle head/tail and empty.

Time Complexity: O(1) for head/tail add/delete; O(n) for index/value ops.
Space Complexity: O(1) per operation.
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


# --- Helpers ---

def array_to_doubly_linked_list(arr):
    """Build doubly linked list from array. Return head."""
    if not arr:
        return None
    head = DoublyListNode(arr[0])
    tail = head
    for i in range(1, len(arr)):
        node = DoublyListNode(arr[i])
        tail.next = node
        node.prev = tail
        tail = node
    return head


def get_tail(head):
    """Return the last node (tail)."""
    if head is None:
        return None
    curr = head
    while curr.next:
        curr = curr.next
    return curr


def list_to_array(head):
    """Convert list to array (head to tail) for testing."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# --- Add Operations ---

def add_at_head(head, val):
    """
    Add a new node with val at the head. Return the new head.

    :type head: DoublyListNode
    :type val: int
    :rtype: DoublyListNode
    """
    node = DoublyListNode(val)

    if not head:
        return node 

    node.next = head
    head.prev = node

    return node


def add_at_tail(head, val):
    """
    Add a new node with val at the tail. Return the head (same if non-empty).

    :type head: DoublyListNode
    :type val: int
    :rtype: DoublyListNode
    """
    node = DoublyListNode(val)

    if not head:
        return node 

    curr = head 
    while curr.next:
        curr = curr.next 

    curr.next = node 
    node.prev = curr

    return head


def add_at_index(head, index, val):
    """
    Add a new node with val at the given index (0-based).
    If index is 0, add at head. Return the head.

    :type head: DoublyListNode
    :type index: int
    :type val: int
    :rtype: DoublyListNode
    """
    if index <= 0:
        return add_at_head(head, val)

    if head is None:
        return DoublyListNode(val)

    node = DoublyListNode(val)
    curr = head
    for _ in range(index):
        if curr.next is None:
            curr.next = node
            node.prev = curr
            return head
        curr = curr.next

    prev = curr.prev
    prev.next = node
    node.prev = prev
    node.next = curr
    curr.prev = node
    return head



# --- Delete Operations ---

def delete_at_head(head):
    """
    Delete the head node. Return the new head (or None if list becomes empty).

    :type head: DoublyListNode
    :rtype: DoublyListNode
    """
    if head is None or head.next is None:
        return None

    head = head.next 
    head.prev = None
    return head


def delete_at_tail(head):
    """
    Delete the tail node. Return the head.

    :type head: DoublyListNode
    :rtype: DoublyListNode
    """
    if head is None or head.next is None:
        return None

    curr = head 
    while curr.next.next:
        curr = curr.next 

    curr.next = None 
    
    return head
    

def delete_by_value(head, val):
    """
    Delete the first node with the given value. Return the head.

    :type head: DoublyListNode
    :type val: int
    :rtype: DoublyListNode
    """
    if head is None:
        return None
    
    if head.val == val:
        new_head = head.next 
        if new_head:
            new_head.prev = None
        return new_head

    curr = head 
    while curr:
        if curr.val == val:
            prev = curr.prev 
            prev.next = curr.next
            if curr.next: 
                curr.next.prev =  prev 

            return head 

        curr = curr.next 

    return head 



def delete_at_index(head, index):
    """
    Delete the node at the given index (0-based). Return the head.

    :type head: DoublyListNode
    :type index: int
    :rtype: DoublyListNode
    """
    if head is None:
        return None

    if index == 0:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head

    curr = head
    while index > 0 and curr:
        curr = curr.next
        index -= 1

    if curr is None:
        return head

    prev = curr.prev
    prev.next = curr.next
    if curr.next:
        curr.next.prev = prev
    return head

if __name__ == "__main__":
    # --- add_at_head ---
    head = array_to_doubly_linked_list([2, 3])
    head = add_at_head(head, 1)
    run_test(list_to_array(head), [1, 2, 3], "add_at_head(1) to [2,3]")
    head = add_at_head(None, 5)
    run_test(list_to_array(head), [5], "add_at_head(5) to empty")
    head = array_to_doubly_linked_list([10])
    head = add_at_head(head, 9)
    run_test(list_to_array(head), [9, 10], "add_at_head(9) to single node [10]")
    head = array_to_doubly_linked_list([3, 4, 5])
    head = add_at_head(head, 2)
    head = add_at_head(head, 1)
    run_test(list_to_array(head), [1, 2, 3, 4, 5], "add_at_head twice [2],[1] to [3,4,5]")
    head = add_at_head(None, 0)
    run_test(list_to_array(head), [0], "add_at_head(0) to empty")
    head = array_to_doubly_linked_list([1, 2, 3, 4, 5])
    head = add_at_head(head, -1)
    run_test(list_to_array(head), [-1, 1, 2, 3, 4, 5], "add_at_head(-1) to [1,2,3,4,5]")

    # --- add_at_tail ---
    head = array_to_doubly_linked_list([1, 2])
    head = add_at_tail(head, 3)
    run_test(list_to_array(head), [1, 2, 3], "add_at_tail(3) to [1,2]")
    head = add_at_tail(None, 7)
    run_test(list_to_array(head), [7], "add_at_tail(7) to empty")

    # --- add_at_index ---
    head = array_to_doubly_linked_list([1, 3])
    head = add_at_index(head, 1, 2)
    run_test(list_to_array(head), [1, 2, 3], "add_at_index(1, 2) to [1,3]")
    head = array_to_doubly_linked_list([2, 3])
    head = add_at_index(head, 0, 1)
    run_test(list_to_array(head), [1, 2, 3], "add_at_index(0, 1) to [2,3]")

    # --- delete_at_head ---
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_at_head(head)
    run_test(list_to_array(head), [2, 3], "delete_at_head [1,2,3]")
    head = array_to_doubly_linked_list([1])
    head = delete_at_head(head)
    run_test(list_to_array(head) if head else [], [], "delete_at_head single node")
    head = array_to_doubly_linked_list([1, 2])
    head = delete_at_head(head)
    run_test(list_to_array(head), [2], "delete_at_head two nodes [1,2]")
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_at_head(head)
    head = delete_at_head(head)
    run_test(list_to_array(head), [3], "delete_at_head twice [1,2,3]")
    head = array_to_doubly_linked_list([1, 2, 3, 4, 5])
    head = delete_at_head(head)
    run_test(list_to_array(head), [2, 3, 4, 5], "delete_at_head [1,2,3,4,5]")
    head = delete_at_head(None)
    run_test(list_to_array(head) if head else [], [], "delete_at_head empty list")

    # --- delete_at_tail ---
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_at_tail(head)
    run_test(list_to_array(head), [1, 2], "delete_at_tail [1,2,3]")
    head = array_to_doubly_linked_list([1])
    head = delete_at_tail(head)
    run_test(list_to_array(head) if head else [], [], "delete_at_tail single node")
    head = array_to_doubly_linked_list([1, 2])
    head = delete_at_tail(head)
    run_test(list_to_array(head), [1], "delete_at_tail two nodes [1,2]")
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_at_tail(head)
    head = delete_at_tail(head)
    run_test(list_to_array(head), [1], "delete_at_tail twice [1,2,3]")
    head = array_to_doubly_linked_list([1, 2, 3, 4, 5])
    head = delete_at_tail(head)
    run_test(list_to_array(head), [1, 2, 3, 4], "delete_at_tail [1,2,3,4,5]")
    head = delete_at_tail(None)
    run_test(list_to_array(head) if head else [], [], "delete_at_tail empty list")

    # --- delete_by_value ---
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_by_value(head, 2)
    run_test(list_to_array(head), [1, 3], "delete_by_value(2) [1,2,3]")
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_by_value(head, 1)
    run_test(list_to_array(head), [2, 3], "delete_by_value(1) head")
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_by_value(head, 3)
    run_test(list_to_array(head), [1, 2], "delete_by_value(3) tail [1,2,3]")
    head = array_to_doubly_linked_list([5])
    head = delete_by_value(head, 5)
    run_test(list_to_array(head) if head else [], [], "delete_by_value(5) single node")
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_by_value(head, 99)
    run_test(list_to_array(head), [1, 2, 3], "delete_by_value(99) not found")
    head = delete_by_value(None, 1)
    run_test(list_to_array(head) if head else [], [], "delete_by_value empty list")
    head = array_to_doubly_linked_list([1, 2])
    head = delete_by_value(head, 2)
    run_test(list_to_array(head), [1], "delete_by_value(2) two nodes [1,2]")
    head = array_to_doubly_linked_list([1, 2, 2, 3])
    head = delete_by_value(head, 2)
    run_test(list_to_array(head), [1, 2, 3], "delete_by_value(2) first occurrence [1,2,2,3]")

    # --- delete_at_index ---
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_at_index(head, 1)
    run_test(list_to_array(head), [1, 3], "delete_at_index(1) [1,2,3]")
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_at_index(head, 0)
    run_test(list_to_array(head), [2, 3], "delete_at_index(0) [1,2,3]")
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_at_index(head, 2)
    run_test(list_to_array(head), [1, 2], "delete_at_index(2) tail [1,2,3]")
    head = array_to_doubly_linked_list([7])
    head = delete_at_index(head, 0)
    run_test(list_to_array(head) if head else [], [], "delete_at_index(0) single node")
    head = delete_at_index(None, 0)
    run_test(list_to_array(head) if head else [], [], "delete_at_index empty list")
    head = array_to_doubly_linked_list([1, 2])
    head = delete_at_index(head, 1)
    run_test(list_to_array(head), [1], "delete_at_index(1) two nodes [1,2]")
    head = array_to_doubly_linked_list([1, 2, 3, 4, 5])
    head = delete_at_index(head, 2)
    run_test(list_to_array(head), [1, 2, 4, 5], "delete_at_index(2) [1,2,3,4,5]")
    head = array_to_doubly_linked_list([1, 2, 3])
    head = delete_at_index(head, 5)
    run_test(list_to_array(head), [1, 2, 3], "delete_at_index(5) out of bounds")
