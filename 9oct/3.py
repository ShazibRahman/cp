# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head=tail=ListNode(0)
        while l1 and l2 :
            if l1.val==l2.val:
                node=ListNode(l1.val)
                tail.next=node
                tail=tail.next
                node=ListNode(l2.val)
                tail.next=node
                tail=tail.next
                l1 = l1.next
                l2 = l2.next
            elif l1.val > l2.val:
                node=ListNode(l2.val)
                tail.next=node
                tail=tail.next
                l2=l2.next
            else:
                node=ListNode(l1.val)


                tail.next=node
                tail=tail.next
                l1=l1.next
        while l1:
                node=ListNode(l1.val)
                tail.next=node
                tail=tail.next
                l1=l1.next
        while l2:
                node=ListNode(l2.val)
                tail.next=node
                tail=tail.next
                l2=l2.next
        return head.next
