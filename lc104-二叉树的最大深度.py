# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from __future__ import annotations  # 注解延迟求值：本地没有 TreeNode 定义也不会报 NameError
from typing import Optional


class Solution:
    # 难度：Easy
    # 难点：递归函数的"语义"要钉死 —— maxDepth 返回的是以当前节点为根的子树高度，
    #       空树返回 0；只有语义明确，才能对左右子树同层调用、再 +1 补上自己这一层。
    # 思路：后序遍历（自底向上）。先递归求出左右子树高度，取较大者 + 1 作为本节点高度。
    # 复杂度：时间 O(n)（每个节点访问一次），空间 O(h)（递归栈深度，最坏链状树 h=n）
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
