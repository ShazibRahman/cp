# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        dict = {}

        i = 0
        while head:

            dict[i] = head
            head = head.next
            i += 1


        midIndex = i // 2

        return dict[midIndex]
