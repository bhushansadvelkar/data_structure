"""
1382. Balance a Binary Search Tree
https://leetcode.com/problems/balance-a-binary-search-tree/

Difficulty: Medium
Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree, Divide and Conquer


Problem:
--------
Given the root of a binary search tree, return a balanced binary search tree
with the same node values.

A binary search tree is balanced if the depth of the two subtrees of every node
never differs by more than 1. If multiple solutions exist, return any of them.

Examples:
---------
Example 1:
    Input: root = [1, null, 2, null, 3, null, 4, null, null]
    Output: [2, 1, 3, null, null, null, 4]
    Note: [3, 1, 4, null, 2, null, null] is also a valid answer.

Example 2:
    Input: root = [2, 1, 3]
    Output: [2, 1, 3]

Constraints:
------------
- The number of nodes in the tree is in the range [1, 10^4].
- 1 <= Node.val <= 10^5
- All Node.val are unique.

Approach: How I solved it
-------------------------
1. Inorder traverse the BST to get a sorted list of values (BST inorder is sorted).
2. Build a balanced BST from the sorted array: pick the middle element as root,
   recursively build left subtree from left..mid-1 and right subtree from mid+1..right.
   Base case: left > right → return None.

Time Complexity: O(n)
    - Inorder traversal visits each node once: O(n).
    - Building the balanced tree visits each value once: O(n).

Space Complexity: O(n)
    - Inorder list stores n values: O(n).
    - Recursion stack for build: O(log n) for the balanced tree.
    - Overall: O(n).
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
    def inorder(self, root, inorder):
        if root == None:
            return
        self.inorder(root.left, inorder)
        inorder.append(root.val)
        self.inorder(root.right, inorder)

    def constructBST(self, inorder, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(inorder[mid])
        root.left = self.constructBST(inorder, left, mid - 1)
        root.right = self.constructBST(inorder, mid + 1, right)
        return root

    def balanceBST(self, root):
        """
        Return a balanced BST with the same node values.

        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder = []
        self.inorder(root, inorder)
        tree = self.constructBST(inorder, 0, len(inorder) - 1)
        return tree


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


def inorder(root):
    """Return inorder traversal (sorted values for a BST)."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def height(root):
    """Return height of tree (-1 for empty)."""
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root):
    """Return True if depth of two subtrees of every node differs by at most 1."""
    if not root:
        return True
    lh, rh = height(root.left), height(root.right)
    if abs(lh - rh) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


if __name__ == "__main__":
    s = Solution()
    # Example 1: skewed 1 -> 2 -> 3 -> 4 (level-order with nulls for missing left children)
    root1 = build_tree([1, None, 2, None, 3, None, 4, None, None])
    new1 = s.balanceBST(root1)
    run_test(inorder(new1) if new1 else None, [1, 2, 3, 4], "Example 1 inorder")
    run_test(is_balanced(new1) if new1 else False, True, "Example 1 balanced")

    # Example 2: already balanced
    root2 = build_tree([2, 1, 3])
    new2 = s.balanceBST(root2)
    run_test(inorder(new2) if new2 else None, [1, 2, 3], "Example 2 inorder")
    run_test(is_balanced(new2) if new2 else False, True, "Example 2 balanced")
