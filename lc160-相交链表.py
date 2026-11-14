from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 难点：两个链表长度不等，直接同步走会在短的那条上先到底；这是「走完全长找差」
    # 而不是「让尾部成环」——后者改动了数据结构，题目不允许。
    # 思路：pA 走到头就换到 headB 起点，pB 走到头换到 headA。两者都恰好走 m+n 步，
    # 若相交，此时必然同时落在第一个公共节点（a+c+b == b+c+a）；若不相交，会同时变成
    # None 从而退出循环，正好返回 None。
    # 复杂度：时间 O(m+n)，空间 O(1)。
    def getIntersectionNode(
        self, headA: Optional[ListNode], headB: Optional[ListNode]
    ) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
