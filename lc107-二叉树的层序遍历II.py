# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    # 难点：想到先自上而下数一遍，再反转；若是头部插入即result.insert(0,level_values)则复杂度变为O(n2)
    # 思路：将自上而下的二叉树的层序遍历进行反转即可得到
    # 复杂度：代码展示的时间复杂度和空间复杂度均为O(n)
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_values = []
            for _ in range(level_size):
                node = queue.popleft
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_values)
        return result[::-1]
