# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy=head
        st=[]
        while dummy:
            st.append(dummy.val)
            dummy=dummy.next


        return st==st[::-1]
