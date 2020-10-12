# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyhead=ListNode(0)
        curr=dummyhead
        carry=0
        while l1 and l2:
            total=l1.val+l2.val+carry
            curr.next=ListNode(total%10)
            carry=total//10
            l1=l1.next
            l2=l2.next
            curr=curr.next
        while l1:
            total=l1.val+carry
            curr.next=ListNode(total%10)
            carry=total//10
            l1=l1.next
            curr=curr.next
        while l2:
            total=l2.val+carry
            curr.next=ListNode(total%10)
            carry=total//10
            l2=l2.next
            curr=curr.next
        if carry>0:
            curr.next=ListNode(carry)

        return dummyhead.next


# i solved it long ago
