# Definition for a binary tree node.

from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 难点：后序是左右中，因此result.append写在最后
    # 思路：后序 = 左子树 -> 右子树 -> 根节点
    # 复杂度：时间复杂度是O(n),空间复杂度是O(h)
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result
