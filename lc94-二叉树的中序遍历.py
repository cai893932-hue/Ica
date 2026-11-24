# Definition for a binary tree node.

from __future__ import annotations
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> List[int]:
        # 难点：append 必须卡在两次递归调用之间——先递归左、再记根、最后递归右；
        # 顺序一挪（比如放最前面）整棵树就从「中序」变成「前序」
        # 思路：左子树 → 根 → 右子树，空节点直接返回；result 由闭包跨层共享
        # 复杂度：时间 O(n)（每节点访问一次）；空间 O(h)（递归栈深 = 树高，最坏 O(n)）
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result
