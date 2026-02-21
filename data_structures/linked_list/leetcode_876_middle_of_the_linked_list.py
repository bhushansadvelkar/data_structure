"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Difficulty: Easy
Topics: Linked List, Two Pointers

Problem:
--------
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes (e.g. list has even length), return the second
middle node.

Examples:
---------
Example 1:
    Input: head = [1, 2, 3, 4, 5]
    Output: [3, 4, 5]
    Explanation: The middle node is 3; the returned list is 3 -> 4 -> 5.

Example 2:
    Input: head = [1, 2, 3, 4, 5, 6]
    Output: [4, 5, 6]
    Explanation: There are two middle nodes (3 and 4); return the second one (4).
    The returned list is 4 -> 5 -> 6.

Constraints:
------------
- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100

How I solved it:
----------------
Fast/slow pointer: move fast two steps and slow one step per iteration. When
fast reaches the end (or fast.next is None), slow is at the middle. For even
length (e.g. 6 nodes), fast stops when it can't advance; slow ends at the
second middle node as required.

Time Complexity: O(n)
    - Single pass; slow traverses roughly n/2 nodes.
Space Complexity: O(1)
    - Only two pointers, no extra data structures.
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
    def middleNode(self, head):
        """
        Return the middle node. If two middles, return the second one.

        :type head: ListNode
        :rtype: ListNode
        """
        fast = head 
        slow = head 

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

        return slow


if __name__ == "__main__":
    sol = Solution()

    run_test(
        list_to_array(sol.middleNode(array_to_list([1, 2, 3, 4, 5]))),
        [3, 4, 5],
        "head=[1,2,3,4,5]",
    )
    run_test(
        list_to_array(sol.middleNode(array_to_list([1, 2, 3, 4, 5, 6]))),
        [4, 5, 6],
        "head=[1,2,3,4,5,6]",
    )
    run_test(
        list_to_array(sol.middleNode(array_to_list([1]))),
        [1],
        "head=[1] single node",
    )
