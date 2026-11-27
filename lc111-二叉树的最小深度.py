from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 难点：None 不是叶子，不能无脑 min(左, 右)+1——一边为空时另一边的 0 会把答案压小。
    # 思路：先判空 → 叶子返回 1 → 只有一边时取那一边的深度 → 两边都在才取 min。
    # 复杂度：时间 O(n)，空间 O(h)（h 为树高，递归栈深度）。
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_depth = float("inf")
        right_depth = float("inf")
        if root.left:
            left_depth = self.minDepth(root.left)
        if root.right:
            right_depth = self.minDepth(root.right)
        return min(left_depth, right_depth) + 1

    # 方法二：BFS 层序遍历。第一个遇到的叶子所在层数就是最小深度。
    # 思路：队列存 (节点, 深度)，层序保证第一次见到的叶子深度最小，直接返回。
    # 复杂度：时间 O(n)，空间 O(w)（w 为最大层宽，队列最长时）。
    # 说明：LeetCode 只会调用 minDepth；这个方法是给你本地对比/学习用的，
    #       本地想测它就手动 Solution().minDepth_bfs(root)。
    def minDepth_bfs(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0
