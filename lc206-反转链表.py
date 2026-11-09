# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from __future__ import annotations

# 难点：理解「头慢慢变尾、尾慢慢变头」这个过程——每次只处理一条边，
#       反转完必须先把 curr 存下来，否则改完 curr.next 就找不到下一站了。
# 思路：prev/curr 两指针（curr.next 提前用元组右值存住），迭代边走边反转；
#       递归则一路走到最后一个节点当 new_head，回溯时把 next 指针掉头。
# 复杂度：迭代 时间 O(n) / 空间 O(1)；递归 时间 O(n) / 空间 O(n)（调用栈）。
class Solution:
    # 迭代法（LeetCode 入口）
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev, curr = None, head
        # 元组右值先整体求值：curr.next 取的是「原来的」下一站，所以不会丢链
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    # 递归法
    def reverseList_rec(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:  # 空链或只剩一个节点：它自己就是新头
            return head
        new_head = self.reverseList_rec(head.next)  # 先把后面的全部反转好
        head.next.next = head  # 让后继指回自己（掉头）
        head.next = None  # 自己变成新尾巴，必须断开，否则成环
        return new_head


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
    cases = [[1, 2, 3, 4, 5], [], [1], [1, 2]]
    for c in cases:
        assert to_list(s.reverseList(build(c))) == c[::-1], c
        assert to_list(s.reverseList_rec(build(c))) == c[::-1], c
    print("全部用例通过：", cases)
