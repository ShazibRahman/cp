# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        cur, prev = head, None
        while cur and cur.next:
            if cur.val != cur.next.val:
                prev = cur
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                if not prev:
                    head = cur.next
                else:
                    prev.next = cur.next
            cur = cur.next
        return head
