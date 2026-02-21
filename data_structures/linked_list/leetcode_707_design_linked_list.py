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
Singly linked list with a head pointer. addAtHead: create node, point to head,
update head. addAtTail: traverse to last node, append. get/addAtIndex/deleteAtIndex:
traverse to the (index-1)-th node, then perform the operation. All index-based
ops require O(index) traversal.

Time Complexity: O(1) for addAtHead; O(n) for addAtTail; O(index) for get/addAtIndex/deleteAtIndex.
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
    Uses same logic as insert_at_head, insert_at_tail, insert_at_index,
    delete_at_head, delete_at_tail, delete_at_index (head-based API).
    """

    def __init__(self):
        """Initialize the linked list."""
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node. Return -1 if index is invalid.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1
        curr = self.head
        for _ in range(index):
            if curr is None:
                return -1
            curr = curr.next
        if curr is None:
            return -1
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element.
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val):
        """
        Append a node of value val as the last element.
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node. If index == length,
        append. If index > length, do nothing.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
            return
        if not self.head:
            return
        node = ListNode(val)
        curr = self.head
        for _ in range(index - 1):
            if curr is None:
                return
            curr = curr.next
        if curr is None:
            return
        node.next = curr.next
        curr.next = node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node if the index is valid.
        :type index: int
        :rtype: None
        """
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        for _ in range(index - 1):
            if curr is None:
                return
            curr = curr.next
        if curr is None or curr.next is None:
            return
        curr.next = curr.next.next


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
    ll = MyLinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)
    run_test(ll.get(1), 2, "get(1) after addAtIndex(1,2)")
    ll.deleteAtIndex(1)
    run_test(ll.get(1), 3, "get(1) after deleteAtIndex(1)")

    # get invalid index
    ll2 = MyLinkedList()
    run_test(ll2.get(0), -1, "get(0) on empty list")
    ll2.addAtHead(1)
    run_test(ll2.get(1), -1, "get(1) when length is 1")

    # addAtTail on empty list
    ll3 = MyLinkedList()
    ll3.addAtTail(5)
    run_test(list_from_my_linked_list(ll3), [5], "addAtTail on empty -> [5]")

    # addAtIndex at 0 (same as addAtHead)
    ll4 = MyLinkedList()
    ll4.addAtHead(2)
    ll4.addAtIndex(0, 1)
    run_test(list_from_my_linked_list(ll4), [1, 2], "addAtIndex(0, 1) -> [1,2]")

    # addAtIndex at end (append)
    ll5 = MyLinkedList()
    ll5.addAtHead(1)
    ll5.addAtHead(2)
    ll5.addAtIndex(2, 3)
    run_test(list_from_my_linked_list(ll5), [2, 1, 3], "addAtIndex(2, 3) append -> [2,1,3]")

    # addAtIndex index > length (no-op)
    ll6 = MyLinkedList()
    ll6.addAtHead(1)
    ll6.addAtIndex(5, 99)
    run_test(list_from_my_linked_list(ll6), [1], "addAtIndex(5,) on len 1 -> unchanged")

    # deleteAtIndex(0) — delete head
    ll7 = MyLinkedList()
    ll7.addAtHead(3)
    ll7.addAtHead(2)
    ll7.addAtHead(1)
    ll7.deleteAtIndex(0)
    run_test(list_from_my_linked_list(ll7), [2, 3], "deleteAtIndex(0) -> [2,3]")

    # deleteAtIndex at end
    ll8 = MyLinkedList()
    ll8.addAtTail(1)
    ll8.addAtTail(2)
    ll8.addAtTail(3)
    ll8.deleteAtIndex(2)
    run_test(list_from_my_linked_list(ll8), [1, 2], "deleteAtIndex(2) last -> [1,2]")

    # deleteAtIndex invalid (no-op)
    ll9 = MyLinkedList()
    ll9.addAtHead(1)
    ll9.addAtTail(2)
    ll9.deleteAtIndex(3)
    run_test(list_from_my_linked_list(ll9), [1, 2], "deleteAtIndex(3) invalid -> unchanged")

    # single node: delete -> empty, get(0) -> -1
    ll10 = MyLinkedList()
    ll10.addAtHead(1)
    ll10.deleteAtIndex(0)
    run_test(ll10.get(0), -1, "single node delete -> get(0) == -1")
    run_test(list_from_my_linked_list(ll10), [], "single node delete -> []")

    # get each index
    ll11 = MyLinkedList()
    for v in [10, 20, 30]:
        ll11.addAtTail(v)
    run_test(ll11.get(0), 10, "get(0)")
    run_test(ll11.get(1), 20, "get(1)")
    run_test(ll11.get(2), 30, "get(2)")
    run_test(ll11.get(3), -1, "get(3) invalid")


