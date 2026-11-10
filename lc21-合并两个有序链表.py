# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from __future__ import annotations


class Solution:
    # 难点：1) while 里每拼好一个节点后要 prev = prev.next 前移，否则后面的
    #          next 全被覆盖到最后一次拼接；2) 循环结束有一边剩一截没拼完，
    #          要整段挂到 prev.next 上（有序链表，剩的直接就有序）。
    # 思路：dummy 哨兵消除「头节点」的特殊性；比较两链当前值，小的一边接上
    #       并前移，最后把没走完的一边整体接上。list1<=list2 时取 list1，
    #       保证稳定（相同元素 list1 在前）。
    # 复杂度：时间 O(m+n)——每步恰好消化一个节点；空间 O(1)——只重接指针，不新建节点。
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        prev = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next  # 关键：拼完一个就要前移，否则新节点被下次覆盖
        prev.next = list1 if list1 else list2  # 循环外：把剩下的一整段接上
        return dummy.next


if __name__ == "__main__":
    class ListNode:  # 本地自测用的最小实现
        def __init__(self, val=0, next=None):
            self.val, self.next = val, next

    def build(vals):
        dummy = tail = ListNode()
        for v in vals:
            tail.next = ListNode(v)
            tail = tail.next
        return dummy.next

    def to_list(node):
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return out

    s = Solution()
    cases = [([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
             ([], [0], [0]),
             ([], [], []),
             ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6])]
    for a, b, want in cases:
        got = to_list(s.mergeTwoLists(build(a), build(b)))
        assert got == want, (a, b, got, want)
    print("全部用例通过：", len(cases), "组")
