"""
1008. Construct Binary Search Tree from Preorder Traversal
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

Difficulty: Medium
Topics: Array, Stack, Tree, Binary Search Tree, Binary Tree

Problem:
--------
Given an array `preorder` representing the preorder traversal of a BST,
construct the tree and return its root.

In a BST:
- left subtree values are smaller than the node value
- right subtree values are greater than the node value

Examples:
---------
Example 1:
    Input: preorder = [8, 5, 1, 7, 10, 12]
    Output: [8, 5, 10, 1, 7, null, 12]

Example 2:
    Input: preorder = [1, 3]
    Output: [1, null, 3]

Constraints:
------------
- 1 <= preorder.length <= 100
- 1 <= preorder[i] <= 1000
- All values of preorder are unique.

How I solved it:
----------------
Use preorder's root-left-right order with BST bounds.
Maintain a shared index into `preorder`.
- If current value does not fit within the allowed `(lower, upper)` range,
  it does not belong in this subtree.
- Otherwise create the node, advance the index, build left subtree with
  `(lower, value)`, then right subtree with `(value, upper)`.

Time Complexity: O(n)
Space Complexity: O(h)
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
    def bstFromPreorder(self, preorder):
        """
        Build a BST from preorder traversal.

        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.idx = 0

        def build(lower, upper):
            if self.idx >= len(preorder):
                return None

            value = preorder[self.idx]
            if value < lower or value > upper:
                return None

            self.idx += 1
            node = TreeNode(value)
            node.left = build(lower, value)
            node.right = build(value, upper)
            return node

        return build(float("-inf"), float("inf"))


def level_order(root):
    """Serialize tree to LeetCode-style level order with trailing nulls trimmed."""
    if not root:
        return []

    from collections import deque

    out = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue

        out.append(node.val)
        q.append(node.left)
        q.append(node.right)

    while out and out[-1] is None:
        out.pop()

    return out


if __name__ == "__main__":
    sol = Solution()

    root1 = sol.bstFromPreorder([8, 5, 1, 7, 10, 12])
    run_test(level_order(root1), [8, 5, 10, 1, 7, None, 12], "preorder=[8,5,1,7,10,12]")

    root2 = sol.bstFromPreorder([1, 3])
    run_test(level_order(root2), [1, None, 3], "preorder=[1,3]")

    root3 = sol.bstFromPreorder([4, 2, 1, 3, 6, 5, 7])
    run_test(level_order(root3), [4, 2, 6, 1, 3, 5, 7], "balanced BST")
