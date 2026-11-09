# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #难点：理解头慢慢变尾，尾慢慢变头的过程
    #思路：prev,curr,next分别对应上一个，当前，下一个。可以用递归和迭代两种方式,递归是走到最后再反转，迭代是边走边反转
    #复杂度：时间是O(n),空间是O(1)

    #迭代法
    def reverseList_iter(self, head: ListNode | None) -> ListNode | None:
        prev , curr = None, head
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
        return prev
    #递归法
    def reverseList_rec(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next
        return head
        new_head = self.reverseList_rec(head.next)
        head.next.next = head
        head,next = None
        return new_head
