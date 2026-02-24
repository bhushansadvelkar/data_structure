"""
430. Flatten a Multilevel Doubly Linked List
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

Difficulty: Medium
Topics: Linked List, Depth-First Search

Problem:
--------
You are given a doubly linked list which in addition to the next and prev pointers,
it could have a child pointer, which may or may not point to a separate doubly
linked list. These child lists may have one or more children of their own, and so on,
to produce a multilevel data structure.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.

Example:
--------
Input:
  1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
  1-2-3-7-8-11-12-9-10-4-5-6-NULL

Constraints:
------------
- The number of nodes is in the range [0, 1000].
- 1 <= Node.val <= 10^5

How I solved it:
----------------
DFS: at each node, if it has a child, flatten the child list, connect current to
child head and child tail to current.next, then set child to None. Recurse.

Time Complexity: O(n)
Space Complexity: O(depth) for recursion stack
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def list_to_array(head):
    """Convert flattened list to array (traverse next only)."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def build_example_list():
    """
    Build the example multilevel list:
    1-2-3-4-5-6 with child 7-8-9-10 under 3, and child 11-12 under 8.
    """
    # Level 1: 1 - 2 - 3 - 4 - 5 - 6
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n1.next, n2.prev = n2, n1
    n2.next, n3.prev = n3, n2
    n3.next, n4.prev = n4, n3
    n4.next, n5.prev = n5, n4
    n5.next, n6.prev = n6, n5

    # Child of 3: 7 - 8 - 9 - 10
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n7.next, n8.prev = n8, n7
    n8.next, n9.prev = n9, n8
    n9.next, n10.prev = n10, n9
    n3.child = n7

    # Child of 8: 11 - 12
    n11 = Node(11)
    n12 = Node(12)
    n11.next, n12.prev = n12, n11
    n8.child = n11

    return n1


def build_simple_list():
    """Single level list 1-2-3."""
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next, n2.prev = n2, n1
    n2.next, n3.prev = n3, n2
    return n1


class Solution(object):
    def flatten(self, head):
        """
        Flatten the multilevel doubly linked list into a single-level list.

        :type head: Node
        :rtype: Node
        """
        pass


if __name__ == "__main__":
    sol = Solution()

    head = build_example_list()
    head = sol.flatten(head)
    run_test(list_to_array(head), [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6], "example")

    head = build_simple_list()
    head = sol.flatten(head)
    run_test(list_to_array(head), [1, 2, 3], "no children")

    head = sol.flatten(None)
    run_test(list_to_array(head) if head else [], [], "empty list")
