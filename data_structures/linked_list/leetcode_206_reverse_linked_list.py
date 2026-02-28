"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Difficulty: Easy
Topics: Linked List, Recursion


Problem:
--------
Given the head of a singly linked list, reverse the list, and return the
reversed list.

Examples:
---------
Example 1:
    Input: head = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

Example 2:
    Input: head = [1, 2]
    Output: [2, 1]

Example 3:
    Input: head = []
    Output: []

Constraints:
------------
- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000

Follow-up:
----------
A linked list can be reversed either iteratively or recursively. Can you
implement both?

How I solved it:
----------------
Iterative: maintain prev and curr; at each step set curr.next = prev, then
advance prev = curr and curr = next. Return prev as new head.

Time Complexity: O(n)
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


class Solution(object):
    def reverseList(self, head):
        """
        Reverse the linked list and return the new head.

        :type head: ListNode
        :rtype: ListNode
        """
        curr = head 
        prev = None 
        next = None 

        while curr:
            next = curr.next 
            curr.next = prev 
            prev = curr
            curr = next 


        return prev 


if __name__ == "__main__":
    sol = Solution()
    run_test(
        list_to_array(sol.reverseList(array_to_list([1, 2, 3, 4, 5]))),
        [5, 4, 3, 2, 1],
        "head=[1,2,3,4,5]",
    )
    run_test(
        list_to_array(sol.reverseList(array_to_list([1, 2]))),
        [2, 1],
        "head=[1,2]",
    )
    run_test(
        list_to_array(sol.reverseList(array_to_list([]))),
        [],
        "head=[] empty",
    )
