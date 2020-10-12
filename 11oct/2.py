# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        st=""
        while head:
            st+=str(head.val)
            head=head.next
        return int(st,2)

depend too much on python but 81% faster and 100% less space usage
