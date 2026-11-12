# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from __future__ import annotations


class Solution:
    # 难点：在fast走到None时，如何利用slow将n点删去
    # 思路：同样采用双指针法进行一趟扫描，发现fast走到None时，slow恰好是n点的前一个点
    #     利用slow.next = slow.next.next即可删去n点
    # 复杂度：时间复杂度为O(L),即列表长度，空间复杂度是O(1)
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
