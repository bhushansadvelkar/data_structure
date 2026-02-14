"""
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/

Difficulty: Easy
Topics: Stack, Tree, Depth-First Search, Binary Tree

Problem:
--------
Given the root of a binary tree, return the postorder traversal of its nodes' values.
Postorder: Left -> Right -> Root.

Examples:
---------
Example 1:
    Input: root = [1, null, 2, 3]
    Output: [3, 2, 1]
    Explanation: 1 is root; 2 is right child of 1; 3 is left child of 2.
    Postorder: left(1)=none, right(1)=2 -> left(2)=3, right(2)=none, visit 3, visit 2, visit 1.

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [1]
    Output: [1]

Constraints:
------------
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Follow-up:
----------
Recursive solution is trivial, could you do it iteratively?

Approach:
---------
(TODO: describe how you solved it)

Time Complexity: O(?)
Space Complexity: O(?)
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
    def postorderTraversal(self, root):
        """
        Return postorder traversal (left, right, root) of the tree as a list.

        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.generate_post_order_traversal(root)
        return self.result

    def get_post_order_traversal(self, root):
        if root is None:
            return None 

        self.get_post_order_traversal(root.left)
        self.generate_post_order_traversal(root.right)
        self.result.append(root.val)


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
    root1 = build_tree([1, None, 2, 3])
    run_test(s.postorderTraversal(root1), [3, 2, 1], "[1,null,2,3]")
    run_test(s.postorderTraversal(None), [], "empty tree")
    root3 = build_tree([1])
    run_test(s.postorderTraversal(root3), [1], "[1]")
