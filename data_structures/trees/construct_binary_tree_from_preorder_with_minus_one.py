"""
Construct Binary Tree From Preorder Sequence With -1 As Null Marker

Difficulty: Medium
Topics: Tree, Recursion, Binary Tree

Problem:
--------
You are given a preorder traversal sequence of a binary tree where `-1`
represents a missing node.

Construct the binary tree and return its root.

Preorder order is:
    root -> left -> right

Example:
--------
    preorder = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]

Builds the tree:

            1
          /   \
         2     3
              / \
             4   5

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


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTreeFromPreorder(self, preorder):
        """
        Build binary tree from preorder traversal with -1 as null marker.

        :type preorder: List[int]
        :rtype: TreeNode
        """
        pass


def preorder_with_minus_one(root):
    """Serialize tree to preorder with -1 for nulls (used by tests)."""
    out = []

    def dfs(node):
        if node is None:
            out.append(-1)
            return
        out.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return out


if __name__ == "__main__":
    sol = Solution()

    preorder1 = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]
    root1 = sol.buildTreeFromPreorder(preorder1)
    run_test(preorder_with_minus_one(root1), preorder1, "example tree")

    preorder2 = [1, 2, 3, -1, -1, -1, -1]
    root2 = sol.buildTreeFromPreorder(preorder2)
    run_test(preorder_with_minus_one(root2), preorder2, "left skewed tree")

    preorder3 = [1, -1, 2, -1, 3, -1, -1]
    root3 = sol.buildTreeFromPreorder(preorder3)
    run_test(preorder_with_minus_one(root3), preorder3, "right skewed tree")

    preorder4 = [-1]
    root4 = sol.buildTreeFromPreorder(preorder4)
    run_test(preorder_with_minus_one(root4), preorder4, "empty tree")
