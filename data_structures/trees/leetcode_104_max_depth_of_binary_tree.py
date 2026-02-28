"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Difficulty: Easy
Topics: Tree, Depth-First Search, Binary Tree


Problem:
--------
Given the root of a binary tree, return its maximum depth.
Maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Examples:
---------
Example 1:
    Input: root = [3, 9, 20, null, null, 15, 7]
    Output: 3

Example 2:
    Input: root = [1, null, 2]
    Output: 2

Constraints:
------------
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100

Approach: How I solved it
-------------------------
- Base case: if root is None, return 0 (empty tree has depth 0).
- Recursively get depth of left and right subtrees.
- Max depth at current node = 1 + max(left_depth, right_depth).
- Visit each node once, so one recursive call per node.

Time Complexity: O(n)
    - n = number of nodes. Each node is visited once.

Space Complexity: O(h)
    - h = height of tree. Recursion call stack depth is at most h (O(n) worst case for skewed tree).
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Time: O(n) - each node visited once.
        Space: O(h) - recursion stack depth, h = tree height (O(n) worst for skewed tree).
        """
        if not root:
            return 0 

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


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
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    run_test(s.maxDepth(root1), 3, "[3,9,20,null,null,15,7]")
    root2 = build_tree([1, None, 2])
    run_test(s.maxDepth(root2), 2, "[1,null,2]")
    run_test(s.maxDepth(None), 0, "empty tree")
    root3 = build_tree([1])
    run_test(s.maxDepth(root3), 1, "[1]")
