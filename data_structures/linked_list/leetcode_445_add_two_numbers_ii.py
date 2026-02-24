"""
445. Add Two Numbers II
https://leetcode.com/problems/add-two-numbers-ii/

Difficulty: Medium
Topics: Linked List, Math, Stack

Problem:
--------
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first, and each of their nodes contains a single
digit. Add the two numbers and return the sum as a linked list (most significant
digit first).

Examples:
---------
Example 1:
    Input: l1 = [7,2,4,3], l2 = [5,6,4]
    Output: [7,8,0,7]
    Explanation: 7243 + 564 = 7807

Example 2:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [8,0,7]
    Explanation: 243 + 564 = 807

Example 3:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Constraints:
------------
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- The list represents a number that does not have leading zeros.

Follow-up: Could you solve it without reversing the input lists?

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
    def reverse_ll(self, head):
        curr = head 
        prev = None 
        next = None 

        while curr:
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 

        return prev 


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

        l1 = self.reverse_ll(l1)
        l2 = self.reverse_ll(l2)

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

        return self.reverse_ll(head) 


if __name__ == "__main__":
    sol = Solution()

    run_test(
        list_to_array(sol.addTwoNumbers(array_to_list([7, 2, 4, 3]), array_to_list([5, 6, 4]))),
        [7, 8, 0, 7],
        "l1=[7,2,4,3] l2=[5,6,4]",
    )
    run_test(
        list_to_array(sol.addTwoNumbers(array_to_list([2, 4, 3]), array_to_list([5, 6, 4]))),
        [8, 0, 7],
        "l1=[2,4,3] l2=[5,6,4]",
    )
    run_test(
        list_to_array(sol.addTwoNumbers(array_to_list([0]), array_to_list([0]))),
        [0],
        "l1=[0] l2=[0]",
    )
