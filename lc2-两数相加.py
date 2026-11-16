# Definition for singly-linked list.

from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 难点：进位要一直传递到链表末尾——最长那位相加仍>=10时，得再挂一个新结点
    # 思路：哑结点 dummy 统一头节点处理；carry 存进位，while l1 or l2 or carry 保证最后的进位不丢
    # 复杂度：时间 O(max(m,n))，遍历较长链表一遍；额外空间 O(1)（输出结点不计入）
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
