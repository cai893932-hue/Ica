# Definition for a binary tree node.

from __future__ import annotations
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> List[int]:
        # 难点：遍历顺序是「根在左右子树之前」——递归三行里 append 必须放在两个 dfs 调用前；
        # result 定义在外层、由闭包共享，各层递归往同一个列表追加，最后整体返回
        # 思路：前序 = 根 → 左子树 → 右子树，空节点直接返回
        # 复杂度：时间 O(n)（每个节点访问一次）；空间 O(h)（递归栈深 = 树高，最坏 O(n)）
        result = []

        def dfs(node):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result
