"""
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Difficulty: Easy
Topics: Linked List


Problem:
--------
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.

Examples:
---------
Example 1:
    Input: head = [1, 1, 2]
    Output: [1, 2]

Example 2:
    Input: head = [1, 1, 2, 3, 3]
    Output: [1, 2, 3]

Constraints:
------------
- The number of nodes is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

Approach:
---------
Walk the list with one pointer; when curr.next exists and curr.val == curr.next.val,
skip the next node (curr.next = curr.next.next). Otherwise advance curr.
Return head.

Time Complexity: O(n)
    - Single pass.

Space Complexity: O(1)
    - In-place; only a few pointers.
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


class Solution(object):
    def deleteDuplicates(self, head):
        """
        Remove duplicate nodes so each value appears once. List stays sorted.

        Code: One pointer current. While current.next exists and current.val ==
        current.next.val, set current.next = current.next.next. Else advance.

        Time: O(n). Space: O(1).
        :type head: ListNode
        :rtype: ListNode
        """
        current = head 
        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next 
        return head


if __name__ == "__main__":
    sol = Solution()
    run_test(
        list_to_array(sol.deleteDuplicates(array_to_list([1, 1, 2]))),
        [1, 2],
        "head=[1,1,2]",
    )
    run_test(
        list_to_array(sol.deleteDuplicates(array_to_list([1, 1, 2, 3, 3]))),
        [1, 2, 3],
        "head=[1,1,2,3,3]",
    )
