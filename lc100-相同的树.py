# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 难点：结构与值必须同时相同；任一层出现一方为 None 或值不等即判不同
    # 思路：直接同步递归两棵树——双空 True、单空 False、值不同 False，
    #       否则继续比较左右子树（&& 短路，左不等就不必再看右）
    # 复杂度：时间 O(n)（每个节点最多访问一次），空间 O(h)（递归栈深度）
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
