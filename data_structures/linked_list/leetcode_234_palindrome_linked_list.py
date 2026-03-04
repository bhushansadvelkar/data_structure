"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Difficulty: Easy
Topics: Linked List, Two Pointers, Stack, Recursion

Problem:
--------
Given the head of a singly linked list, return true if it is a palindrome or
false otherwise.

Examples:
---------
Example 1:
    Input: head = [1, 2, 2, 1]
    Output: true

Example 2:
    Input: head = [1, 2]
    Output: false

Constraints:
------------
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Follow-up:
----------
Could you do it in O(n) time and O(1) space?

How I solved it:
----------------
(TODO)

Time Complexity: O(?)
Space Complexity: O(?)
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


class Solution(object):
    def _reverse(self, head):
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        return prev

    def _copy_list(self, head):
        """Build a copy of the list (needed since reverse modifies in place)."""
        if not head:
            return None
        dummy = ListNode(0)
        p = dummy
        while head:
            p.next = ListNode(head.val)
            p, head = p.next, head.next
        return dummy.next

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        orig = self._copy_list(head)
        rev = self._reverse(head)

        while orig:
            if orig.val != rev.val:
                return False
            orig, rev = orig.next, rev.next
        return True 


if __name__ == "__main__":
    sol = Solution()

    run_test(sol.isPalindrome(array_to_list([1, 2, 2, 1])), True, "Example 1: [1,2,2,1]")
    run_test(sol.isPalindrome(array_to_list([1, 2])), False, "Example 2: [1,2]")
    run_test(sol.isPalindrome(array_to_list([1, 1, 2, 1])), False, "[1,1,2,1]")
