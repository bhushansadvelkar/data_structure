"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Difficulty: Easy
Topics: Linked List, Hash Table, Two Pointers

Problem:
--------
Given head, the head of a linked list, determine if the linked list has a cycle.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is
used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Examples:
---------
Example 1:
    Input: head = [3, 2, 0, -4], pos = 1
    Output: true
    Explanation: There is a cycle where tail connects to the 1st node (0-indexed).

Example 2:
    Input: head = [1, 2], pos = 0
    Output: true
    Explanation: There is a cycle where tail connects to the 0th node.

Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle.

Constraints:
------------
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked list.

Approach:
---------
Floyd's cycle detection (slow/fast pointers): slow moves 1 step, fast moves 2
steps. If there is a cycle, fast will eventually meet slow. If fast reaches
None, no cycle.

Time Complexity: O(n)
Space Complexity: O(1)

Approach Diagram - Floyd (Mermaid):
----------------------------------
```mermaid
flowchart TD
    A[slow=fast=head] --> B{fast and fast.next?}
    B -->|No| C[Return False]
    B -->|Yes| D[slow=1 step fast=2 steps]
    D --> E{slow == fast?}
    E -->|Yes| F[Return True cycle]
    E -->|No| B
```
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list_with_cycle(arr, pos):
    """
    Build linked list from list. If pos >= 0, connect tail to node at index pos.
    pos == -1 means no cycle.
    """
    if not arr:
        return None
    dummy = ListNode(0)
    p = dummy
    nodes = []
    for x in arr:
        p.next = ListNode(x)
        p = p.next
        nodes.append(p)
    if 0 <= pos < len(nodes):
        p.next = nodes[pos]
    return dummy.next


class Solution(object):
    def hasCycle(self, head):
        """
        Return True if the linked list has a cycle, else False.

        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True 
            
            slow = slow.next 
            fast = fast.next.next 

        return False


if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.hasCycle(build_list_with_cycle([3, 2, 0, -4], 1)),
        True,
        "head=[3,2,0,-4], pos=1",
    )
    run_test(
        sol.hasCycle(build_list_with_cycle([1, 2], 0)),
        True,
        "head=[1,2], pos=0",
    )
    run_test(
        sol.hasCycle(build_list_with_cycle([1], -1)),
        False,
        "head=[1], pos=-1",
    )
