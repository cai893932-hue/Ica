# Definition for a binary tree node.

from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #难点：遍历顺序是左中右，append要放在中间
    #思路：左子树 -> 根 -> 右子树，空节点直接返回
    #复杂度：时间复杂度是O(n),空间复杂度是O(h)
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        def def(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result
