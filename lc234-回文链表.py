# Definition for singly-linked list.

from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 难点：反转后比较时，循环条件必须由反转半段 right 驱动而非 left。
    #       这样奇偶长度天然统一：偶数时 slow 落在后半段起点，奇数时 slow 就是正中间那个节点，
    #       它会被反转进半段，最后和自己比一次（多余但无害）。若写成 while left 或固定比较 n//2 次，
    #       奇数长度就会越界或漏比。
    # 思路：快慢指针找中点 → 就地反转后半段 → 双指针从两端向中间比对；
    #       不改链表的话可以直接压栈，但那样要 O(n) 额外空间。
    # 复杂度：时间 O(n)（找中点 n/2 + 反转 n/2 + 比对 n/2），空间 O(1)（只用了四个指针）
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
