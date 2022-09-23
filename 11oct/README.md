# 11 october (Leetcode)


1. [reverse a linked list](https://leetcode.com/problems/reverse-linked-list/)
```python
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

```
<br>
<br>

2. [convert a binary number in  a linked list to to integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)

```python
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
)
```

> depend too much on python but 81% faster and 100% less space usage

<br>
<br>

3. [middle of a linked list](https://leetcode.com/problems/middle-of-the-linked-list/)

```python
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
```
