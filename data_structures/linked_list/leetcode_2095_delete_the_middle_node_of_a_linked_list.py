"""
2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Difficulty: Medium
Topics: Linked List, Two Pointers

Problem:
--------
You are given the head of a linked list. Delete the middle node, and return the
head of the modified linked list.

The middle node of a linked list of size n is the floor(n / 2)-th node (0-indexed).
- n = 1: middle at index 0
- n = 2: middle at index 1
- n = 3: middle at index 1
- n = 4: middle at index 2

Examples:
---------
Example 1:
    Input: head = [1, 3, 4, 7, 1, 2, 6]
    Output: [1, 3, 4, 1, 2, 6]
    Explanation: n = 7, middle at index 3 (value 7) is deleted.

Example 2:
    Input: head = [1, 2, 3, 4]
    Output: [1, 2, 4]
    Explanation: n = 4, middle at index 2 (value 3) is deleted.

Example 3:
    Input: head = [2, 1]
    Output: [2]
    Explanation: n = 2, middle at index 1 (value 1) is deleted.

Constraints:
------------
- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5

How I solved it:
---------------
Fast/slow pointer to find the middle node. Keep a prev pointer trailing slow.
When fast reaches the end, slow is at the middle; unlink it by setting
prev.next = slow.next. Handle edge cases: empty list and single-node list
return None (no middle to delete in size 1).

Time Complexity: O(n)
    - Single pass to find middle.
Space Complexity: O(1)
    - Only pointers, no extra structures.
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
    def deleteMiddle(self, head):
        """
        Delete the middle node and return the head of the modified list.

        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head 
        if not head:
            return None 

        if head.next is None:
            return None

        while fast and fast.next:
            prev = slow
            fast = fast.next.next 
            slow = slow.next
        
        prev.next = slow.next 

        return head


if __name__ == "__main__":
    sol = Solution()
    run_test(
        list_to_array(sol.deleteMiddle(array_to_list([1, 3, 4, 7, 1, 2, 6]))),
        [1, 3, 4, 1, 2, 6],
        "head=[1,3,4,7,1,2,6]",
    )
    run_test(
        list_to_array(sol.deleteMiddle(array_to_list([1, 2, 3, 4]))),
        [1, 2, 4],
        "head=[1,2,3,4]",
    )
    run_test(
        list_to_array(sol.deleteMiddle(array_to_list([2, 1]))),
        [2],
        "head=[2,1]",
    )
