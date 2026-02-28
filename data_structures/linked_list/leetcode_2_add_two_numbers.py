"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

Difficulty: Medium
Topics: Linked List, Math, Recursion

Problem:
--------
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single
digit. Add the two numbers and return the sum as a linked list in reverse order.

Examples:
---------
Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
------------
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

How I solved it:
----------------
I traversed both linked lists simultaneously with a carry. At each step I add
current digits (or 0 when a list ends), create one node with sum % 10, and
propagate carry = sum // 10. Continue until both lists and carry are done.

Time Complexity: O(max(n, m))
Space Complexity: O(1) extra (excluding output list)
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


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Add two numbers represented as linked lists (digits in reverse order).
        Return the sum as a linked list in reverse order.

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        temp_pointer = None
        carry = 0

        while l1 or l2 or carry:
            element = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = element // 10
            node = ListNode(element % 10)
            if head is None:
                head = node
            else:
                temp_pointer.next = node
            temp_pointer = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head 


if __name__ == "__main__":
    sol = Solution()

    run_test(
        list_to_array(sol.addTwoNumbers(array_to_list([2, 4, 3]), array_to_list([5, 6, 4]))),
        [7, 0, 8],
        "l1=[2,4,3] l2=[5,6,4]",
    )
    run_test(
        list_to_array(sol.addTwoNumbers(array_to_list([0]), array_to_list([0]))),
        [0],
        "l1=[0] l2=[0]",
    )
    run_test(
        list_to_array(sol.addTwoNumbers(array_to_list([9, 9, 9, 9, 9, 9, 9]), array_to_list([9, 9, 9, 9]))),
        [8, 9, 9, 9, 0, 0, 0, 1],
        "l1=[9,9,9,9,9,9,9] l2=[9,9,9,9]",
    )
