# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next=head
        le=0;
        dum=head
        while dum:
            le+=1
            dum=dum.next

        le-=n

        dum=dummy
        while le>0:
            le-=1
            dum=dum.next
        dum.next=dum.next.next
        return dummy.next
