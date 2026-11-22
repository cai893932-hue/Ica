from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 难点：镜像判定不是"对应位置相等"，而是左子树的左 对 右子树的右、左子树的右 对 左子树的左
    # 思路：同时递归比较两对外侧/内侧节点，任一对不等即 False
    # 复杂度：时间 O(n)（每节点比一次），空间 O(h)（递归栈深度 h，最坏 O(n)）
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.is_mirror(left.left, right.right) and self.is_mirror(
            left.right, right.left
        )
