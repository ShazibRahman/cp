# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
         if head is None or head.next is None:
            return
         prev=None
         cur=head
         while cur:
            next_ele=cur.next
            cur.next=prev
            prev=cur
            cur=next_ele
         head=prev
         return head
