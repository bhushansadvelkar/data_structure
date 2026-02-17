"""
707. Design Linked List
https://leetcode.com/problems/design-linked-list/

Difficulty: Medium
Topics: Linked List, Design

Problem:
--------
Design your implementation of the linked list. You can choose to use a singly
or doubly linked list.

A node in a singly linked list should have two attributes: val and next. val
is the value of the current node, and next is a pointer/reference to the next
node. If you want to use the doubly linked list, you will need one more
attribute prev to indicate the previous node in the linked list. Assume all
nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the index-th node. If the index is
  invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element.
  After the insertion, the new node will be the first node.
- void addAtTail(int val) Append a node of value val as the last element.
- void addAtIndex(int index, int val) Add a node of value val before the
  index-th node. If index equals the length of the linked list, the node will
  be appended to the end. If index is greater than the length, do not insert.
- void deleteAtIndex(int index) Delete the index-th node, if the index is valid.

Examples:
---------
Example 1:
    Input:
        ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
         "deleteAtIndex", "get"]
        [[], [1], [3], [1, 2], [1], [1], [1]]
    Output: [null, null, null, null, 2, null, 3]
    Explanation:
        MyLinkedList myLinkedList = new MyLinkedList();
        myLinkedList.addAtHead(1);      // list: 1
        myLinkedList.addAtTail(3);     // list: 1->3
        myLinkedList.addAtIndex(1, 2); // list: 1->2->3
        myLinkedList.get(1);           // return 2
        myLinkedList.deleteAtIndex(1); // list: 1->3
        myLinkedList.get(1);           // return 3

Constraints:
------------
- 0 <= index, val <= 1000
- Do not use the built-in LinkedList library.
- At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex
  and deleteAtIndex.

How I solved it:
----------------
(TODO: describe your approach)

Time Complexity: O(1) for addAtHead/addAtTail; O(index) for get/addAtIndex/deleteAtIndex.
Space Complexity: O(n) for n nodes.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):
    """
    Design Linked List: get, addAtHead, addAtTail, addAtIndex, deleteAtIndex.
    """

    def __init__(self):
        """Initialize the linked list."""
        pass

    def get(self, index):
        """
        Get the value of the index-th node. Return -1 if index is invalid.
        :type index: int
        :rtype: int
        """
        pass

    def addAtHead(self, val):
        """
        Add a node of value val before the first element.
        :type val: int
        :rtype: None
        """
        pass

    def addAtTail(self, val):
        """
        Append a node of value val as the last element.
        :type val: int
        :rtype: None
        """
        pass

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node. If index == length,
        append. If index > length, do nothing.
        :type index: int
        :type val: int
        :rtype: None
        """
        pass

    def deleteAtIndex(self, index):
        """
        Delete the index-th node if the index is valid.
        :type index: int
        :rtype: None
        """
        pass


def list_from_my_linked_list(ll):
    """Convert MyLinkedList to list (for testing). Assumes head is accessible or use get(i)."""
    out = []
    i = 0
    while True:
        v = ll.get(i)
        if v == -1:
            break
        out.append(v)
        i += 1
    return out


if __name__ == "__main__":
    # Example 1: addAtHead(1), addAtTail(3), addAtIndex(1,2), get(1)->2, deleteAtIndex(1), get(1)->3
    # ll = MyLinkedList()
    # ll.addAtHead(1)
    # ll.addAtTail(3)
    # ll.addAtIndex(1, 2)
    # run_test(ll.get(1), 2, "get(1) after addAtIndex(1,2)")
    # ll.deleteAtIndex(1)
    # run_test(ll.get(1), 3, "get(1) after deleteAtIndex(1)")

    # # get invalid index
    # ll2 = MyLinkedList()
    # run_test(ll2.get(0), -1, "get(0) on empty list")
    # ll2.addAtHead(1)
    # run_test(ll2.get(1), -1, "get(1) when length is 1")

    node = ListNode(1)
    print(node.val, node.next)
