# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import annotations


class Solution:
    #难点：在while循环之后，忘记处理剩余节点，连接下一个节点后，忘记保留新的被覆盖节点
    #思路：list1<=list2时，也排在list2前面，一个节点结束之后，处理剩下的节点，利用dummy消除头节点的特殊性
    #复杂度：时间复杂度是O(m+n)，遍历两个节点，空间复杂度是O(1)
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        prev = dummy
        while list1 and list2:
            if list1.val <= list2.val
            prev.next = list1
            list1 = list2.next
            else:
                prev.next = list2
                list2 = list2.next
            prev.next = list1 if list1 else list2
        return dummy.next
