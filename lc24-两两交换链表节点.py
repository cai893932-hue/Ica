# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 难点：指针改接的顺序——node1.next 必须先接上 node2 的原后继（node2.next 还没被覆盖时），
    # 再让 node2.next 指回 node1，顺序反了链就断了；且每轮结束 prev 要前进到 node1（交换后的第二个节点）
    # 思路：利用dummy node，避免如用if判断的单独处理头节点变化的方法。
    # 复杂度：时间复杂度是O(n),空间复杂度是O(1)
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            node1 = prev.next
            node2 = prev.next.next
            prev.next = node2
            node1.next = node2.next
            node2.next = node1
            prev = node1
        return dummy.next
