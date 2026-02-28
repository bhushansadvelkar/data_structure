"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Difficulty: Medium
Topics: Linked List, Two Pointers


Problem:
--------
Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Examples:
---------
Example 1:
    Input: head = [1, 2, 3, 4, 5], n = 2
    Output: [1, 2, 3, 5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1, 2], n = 1
    Output: [1]

Constraints:
------------
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Follow-up:
----------
Could you do this in one pass?

How I solved it:
---------------
Two-pointer: advance fast n steps first. If fast becomes None, the nth-from-end
is the head—return head.next. Otherwise, move both fast and slow until
fast.next is None; slow is then one node before the target. Remove the target
with slow.next = slow.next.next.

Time Complexity: O(n)
    - Single pass; at most n steps.
Space Complexity: O(1)
    - Only two pointers.
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
    def removeNthFromEnd(self, head, n):
        """
        Remove the nth node from the end of the list and return the head.

        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head 

        for i in range(n):
            fast = fast.next 

        if not fast:
            return head.next 

        while fast.next:
            fast = fast.next 
            slow = slow.next 

        slow.next = slow.next.next 

        return head


if __name__ == "__main__":
    sol = Solution()
    run_test(
        list_to_array(sol.removeNthFromEnd(array_to_list([1, 2, 3, 4, 5]), 2)),
        [1, 2, 3, 5],
        "head=[1,2,3,4,5], n=2",
    )
    run_test(
        list_to_array(sol.removeNthFromEnd(array_to_list([1]), 1)),
        [],
        "head=[1], n=1",
    )
    run_test(
        list_to_array(sol.removeNthFromEnd(array_to_list([1, 2]), 1)),
        [1],
        "head=[1,2], n=1",
    )
