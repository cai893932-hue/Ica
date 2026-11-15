# Definition for singly-linked list.

from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 难点：除了栈和数组，想到双指针法，以及找到中点后奇偶长度的处理
    # 思路：先用双指针找中点，再反转链表，最后比较，验证回文列表
    # 复杂度：这套方法的空间复杂度是O(n),时间复杂度是O(1)
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:  # 防御性编程：空链表和只有一个节点的链表
            return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
