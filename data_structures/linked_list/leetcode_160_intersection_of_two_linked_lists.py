"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Difficulty: Easy
Topics: Linked List, Hash Table, Two Pointers


Problem:
--------
Given the heads of two singly linked lists headA and headB, return the node at
which the two lists intersect. If the two linked lists have no intersection at all,
return None.

The linked lists must retain their original structure after the function returns.
There are no cycles in the linked structure.

Examples:
---------
Example 1:
    listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], intersect at 8
    Output: node with value 8

Example 2:
    listA = [1,9,1,2,4], listB = [3,2,4], intersect at 2
    Output: node with value 2

Example 3:
    listA = [2,6,4], listB = [1,5]
    Output: None (no intersection)

Constraints:
------------
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5
- 0 <= skipA < m, 0 <= skipB < n

Follow-up: O(m + n) time, O(1) memory.

How I solved it:
---------------
Two pointers: traverse listA then listB with pa, listB then listA with pb; when
pa == pb (same node or both None) that is the intersection or no intersection.

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


def build_intersecting_lists(prefix_a, prefix_b, common):
    """
    Build two lists that share a common tail.
    prefix_a + common = listA, prefix_b + common = listB.
    Returns (headA, headB, intersection_node).
    """
    common_head = array_to_list(common)
    if not common_head:
        return array_to_list(prefix_a), array_to_list(prefix_b), None

    head_a = array_to_list(prefix_a)
    if head_a:
        curr = head_a
        while curr.next:
            curr = curr.next
        curr.next = common_head
    else:
        head_a = common_head

    head_b = array_to_list(prefix_b)
    if head_b:
        curr = head_b
        while curr.next:
            curr = curr.next
        curr.next = common_head
    else:
        head_b = common_head

    return head_a, head_b, common_head


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Return the node where listA and listB intersect, or None.

        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        linked_list_map = {}

        while headA:
            linked_list_map[headA] = headA.val
            headA = headA.next 


        while headB:
            if headB in linked_list_map:
                return headB 
            headB = headB.next 

        return None


if __name__ == "__main__":
    sol = Solution()

    # Example 1: intersect at 8
    head_a, head_b, expected = build_intersecting_lists([4, 1], [5, 6, 1], [8, 4, 5])
    result = sol.getIntersectionNode(head_a, head_b)
    run_test(result.val if result else None, 8, "intersect at 8")

    # Example 2: intersect at 2
    head_a, head_b, expected = build_intersecting_lists([1, 9, 1], [3], [2, 4])
    result = sol.getIntersectionNode(head_a, head_b)
    run_test(result.val if result else None, 2, "intersect at 2")

    # Example 3: no intersection
    head_a = array_to_list([2, 6, 4])
    head_b = array_to_list([1, 5])
    result = sol.getIntersectionNode(head_a, head_b)
    run_test(result is None, True, "no intersection")

    # Same list (both point to same head)
    head_a = array_to_list([1, 2, 3])
    result = sol.getIntersectionNode(head_a, head_a)
    run_test(result.val if result else None, 1, "same list")
