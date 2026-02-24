"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Difficulty: Easy
Topics: Linked List, Recursion

Problem:
--------
You are given the heads of two sorted linked lists list1 and list2. Merge the two
lists into one sorted list by splicing together the nodes from both input lists.
Return the head of the merged linked list.

Examples:
---------
Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
------------
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

How I solved it:
----------------
Use a dummy head; iterate over both lists, append the smaller node to the tail,
then advance that list. Append remaining nodes. Return dummy.next.

Time Complexity: O(m + n)
Space Complexity: O(1)
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
    """Convert linked list to array."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def array_to_list(arr):
    """Build linked list from array."""
    if not arr:
        return None
    dummy = ListNode(0)
    p = dummy
    for x in arr:
        p.next = ListNode(x)
        p = p.next
    return dummy.next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2 

        if l2 is None:
            return l1 

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    sol = Solution()

    run_test(
        list_to_array(sol.mergeTwoLists(array_to_list([1, 2, 4]), array_to_list([1, 3, 4]))),
        [1, 1, 2, 3, 4, 4],
        "list1=[1,2,4] list2=[1,3,4]",
    )
    run_test(
        list_to_array(sol.mergeTwoLists(array_to_list([]), array_to_list([]))) or [],
        [],
        "both empty",
    )
    run_test(
        list_to_array(sol.mergeTwoLists(array_to_list([]), array_to_list([0]))),
        [0],
        "list1 empty list2=[0]",
    )
