# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 难点：左右孩子必须「同时」交换。写成两句
    #       root.left = invert(root.right); root.right = invert(root.left)
    #       第二句拿到的 left 已经被改过了，会把自己换回来 —— 必须用元组解构一次赋值。
    # 思路：树递归的标准形状 —— 处理自己（交换左右孩子）+ 递归处理左右子树。
    #       不要想着「重新建一棵树」，就地交换指针就够，空节点返回 None 即 base case。
    # 复杂度：时间 O(n)（每个节点恰好访问一次）/ 空间 O(h) 递归栈，h 为树高，链状树最坏 O(n)
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
