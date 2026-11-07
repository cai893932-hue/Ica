# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = self.right = None
from __future__ import annotations
from collections import deque


class Solution:
    # 难点：怎么把"一层"和"下一层"分开——用 level_size 先冻结本层节点数，再逐个出队；
    #       另外列表 queue.pop(0) 是 O(n)（整体前移），必须用 deque.popleft() 才是 O(1)
    # 思路：BFS。队列里只保留"当前层 + 已发现的下一层"节点；每轮先记下本层长度，
    #       弹出恰好 level_size 个并收集 val，把它们的子节点追加到队尾作为下一层
    # 复杂度：每个节点入队/出队各一次，时间 O(n)；队列与 result 最多存一层节点，空间 O(n)
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_values)
        return result
