"""
100. Same Tree
https://leetcode.com/problems/same-tree/

Difficulty: Easy
Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree


Problem:
--------
Given the roots of two binary trees p and q, write a function to check if they
are the same or not. Two binary trees are the same if they are structurally
identical and the nodes have the same value.

Examples:
---------
Example 1:
    Input: p = [1, 2, 3], q = [1, 2, 3]
    Output: True

Example 2:
    Input: p = [1, 2], q = [1, null, 2]
    Output: False
    Explanation: Different structure.

Example 3:
    Input: p = [1, 2, 1], q = [1, 1, 2]
    Output: False
    Explanation: Same structure but different values.

Constraints:
------------
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4

Approach:
---------
Recursive DFS: Two trees are the same iff (1) both roots are None, or (2) both
roots exist with the same value and recursively their left subtrees are the
same and their right subtrees are the same. If one is None and the other is
not, or values differ, return False immediately.

Time Complexity: O(n)
    - Visit each node at most once; n = total nodes in the smaller tree.

Space Complexity: O(h)
    - Recursion stack depth; h = height of the tree. O(log n) for balanced,
      O(n) for skewed.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        Return True if trees p and q are the same, else False.

        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True 
    
        if not p or not q:
            return False

        if p.val != q.val:
            return False
        
        return (
            self.isSameTree(p.right, q.right)
            and 
            self.isSameTree(p.left, q.left)
        )


def build_tree(values):
    """Build tree from list (LeetCode-style: level order, None for null)."""
    if not values:
        return None
    root = TreeNode(values[0])
    from collections import deque
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    s = Solution()
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    run_test(s.isSameTree(p1, q1), True, "p=[1,2,3], q=[1,2,3]")

    p2 = build_tree([1, 2])
    q2 = build_tree([1, None, 2])
    run_test(s.isSameTree(p2, q2), False, "p=[1,2], q=[1,null,2]")

    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    run_test(s.isSameTree(p3, q3), False, "p=[1,2,1], q=[1,1,2]")
