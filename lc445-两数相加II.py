# Definition for singly-linked list.

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 难点：进位处理，两条链表一长一短，如何从最低位相加
    # 思路：想到利用栈“后进先出”的特性，可以实现最低位相加，carry存进位，保证结果
    # 复杂度：时间和空间复杂度都是O(m+n)，遍历两个链表，以及栈所占用的空间
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        head = None
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            new_node = ListNode(digit)
            new_node.next = head
            head = new_node
        return head
