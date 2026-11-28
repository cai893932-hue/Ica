# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 难点：直接层序遍历是 O(n)，没利用「完全二叉树」这条件；满二叉树可直接用高度算节点数
    # 思路：分别沿最左路、最右路量深度；两者相等 => 该树是满二叉树，节点数 2^(h+1)-1
    #      不等则对左右子树递归（完全二叉树的子树依然是完全二叉树）
    #      注意：比较的是「两条路径的深度」，不是「左子树等于右子树」——非满时两子树一般不等
    # 复杂度：时间 O(log²n)（每层量两次高度 O(log n)，递归深度 O(log n)），空间 O(log n) 递归栈
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        left_depth = 0
        left_node = root
        while left_node.left:
            left_depth += 1
            left_node = left_node.left
        right_depth = 0
        right_node = root
        while right_node.right:
            right_depth += 1
            right_node = right_node.right
        if left_depth == right_depth:
            return (1 << (left_depth + 1)) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
