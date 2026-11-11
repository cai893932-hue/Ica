# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from __future__ import annotations

from typing import Optional


class Solution:
    # 难点：链表没有"已访问"标记，怎么在 O(1) 空间里判断自己绕回来了。
    #       关键洞察：快指针相对慢指针每步追近 1 个节点，一旦成环必在环内追上，
    #       且相对速度是 1，不会"跳过头"。
    # 思路：快慢指针（Floyd 判圈）。同起点出发，慢走 1、快走 2；
    #       相遇即有环，快指针先走到 None 即无环。
    # 复杂度：时间 O(n)（快指针最多走 n 步，环长 ≤ n）；空间 O(1)（两个指针）。
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # 空链表 / 单节点走不进循环，直接返回 False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:      # 比"是不是同一个节点"，用 is 比 == 更准确
                return True

        return False


if __name__ == '__main__':
    class ListNode:
        def __init__(self, x, nxt=None):
            self.val = x
            self.next = nxt

    def build(vals, pos):
        """按 pos 把尾节点接回第 pos 个节点，pos=-1 表示无环。"""
        nodes = [ListNode(v) for v in vals]
        for a, b in zip(nodes, nodes[1:]):
            a.next = b
        if pos >= 0:
            nodes[-1].next = nodes[pos]
        return nodes[0] if nodes else None

    s = Solution()
    print(s.hasCycle(build([3, 2, 0, -4], 1)), '-> True')
    print(s.hasCycle(build([1, 2], 0)), '-> True')
    print(s.hasCycle(build([1], -1)), '-> False')
    print(s.hasCycle(build([], -1)), '-> False')
    n = ListNode(7)          # 单节点自环
    n.next = n
    print(s.hasCycle(n), '-> True')
