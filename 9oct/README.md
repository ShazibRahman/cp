# 9 october (Leetcode)

1. [Add two numbers](https://leetcode.com/problems/add-two-numbers/)

```python
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
```

2. [Remove nth node from end of list](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

```python
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
```

3. [Merge two sorted lists](https://leetcode.com/problems/merge-two-sorted-lists/)

```python
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
```

4. [Palindrome linked list](https://leetcode.com/problems/palindrome-linked-list/)

```python
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
```
