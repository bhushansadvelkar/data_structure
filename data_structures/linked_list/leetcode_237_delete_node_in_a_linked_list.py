"""
237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/

Difficulty: Medium
Topics: Linked List

Problem:
--------
Write a function to delete a node in a singly-linked list. You will not be given
access to the head of the list, instead you will be given access to the node
to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Examples:
---------
Example 1:
    Input: head = [4, 5, 1, 9], node = 5
    Output: [4, 1, 9]
    Explanation: You are given the second node with value 5, the linked list
    should become 4 -> 1 -> 9 after calling your function.

Example 2:
    Input: head = [4, 5, 1, 9], node = 1
    Output: [4, 5, 9]
    Explanation: You are given the third node with value 1, the linked list
    should become 4 -> 5 -> 9 after calling your function.

Constraints:
------------
- The number of nodes in the list is in the range [2, 1000].
- -1000 <= Node.val <= 1000
- The value of each node in the list is unique.
- The node to be deleted is in the list and is not a tail node.

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


def find_node(head, val):
    """Return the first node with given value, or None."""
    curr = head
    while curr:
        if curr.val == val:
            return curr
        curr = curr.next
    return None


class Solution(object):
    def deleteNode(self, node):
        """
        Delete the given node from the linked list. Modify in-place.

        :type node: ListNode
        :rtype: None Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val 
        node.next = node.next.next


if __name__ == "__main__":
    sol = Solution()

    # head=[4,5,1,9], delete node 5 -> [4,1,9]
    head = array_to_list([4, 5, 1, 9])
    node = find_node(head, 5)
    sol.deleteNode(node)
    run_test(list_to_array(head), [4, 1, 9], "head=[4,5,1,9] delete 5")

    # head=[4,5,1,9], delete node 1 -> [4,5,9]
    head = array_to_list([4, 5, 1, 9])
    node = find_node(head, 1)
    sol.deleteNode(node)
    run_test(list_to_array(head), [4, 5, 9], "head=[4,5,1,9] delete 1")
