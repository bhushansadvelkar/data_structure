"""
501. Find Mode in Binary Search Tree
https://leetcode.com/problems/find-mode-in-binary-search-tree/

Difficulty: Easy
Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree

Problem:
--------
Given the root of a binary search tree (BST) with duplicates, return all the
mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than or equal
  to the node's key.
- The right subtree of a node contains only nodes with keys greater than or
  equal to the node's key.
- Both the left and right subtrees must also be binary search trees.

Examples:
---------
Example 1:
    Input: root = [1, null, 2, 2]
    Output: [2]
    Explanation: 2 appears twice; 1 appears once. Mode is 2.

Example 2:
    Input: root = [0]
    Output: [0]
    Explanation: Single node, mode is 0.

Constraints:
------------
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5

Follow-up:
----------
Could you do that without using any extra space? (Assume that the implicit
recursion stack does not count.)

How I solved it:
----------------
Postorder traverse to collect all values, count with Counter, find max count,
return all keys whose count equals the max.

Time Complexity: O(n)
Space Complexity: O(n)
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

from collections import Counter

class Solution(object):
    def findMode(self, root):
        """
        Return the mode(s) of the BST.

        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self._postorder(root)
        resultant_dict = Counter(self.result)
        maximum_repetitions = max(resultant_dict.values()) if resultant_dict else 0
        return [key for key, count in resultant_dict.items() if count == maximum_repetitions]

    def _postorder(self, root):
        if root is None:
            return
        self._postorder(root.left)
        self._postorder(root.right)
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
    sol = Solution()
    run_test(
        sorted(sol.findMode(build_tree([1, None, 2, 2]))),
        [2],
        "root=[1,null,2,2]",
    )
    run_test(sol.findMode(build_tree([0])), [0], "root=[0]")
