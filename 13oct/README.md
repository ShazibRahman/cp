# 13 oct Leetcode

## stacks questions
1. [game of two stacks](https://www.hackerrank.com/challenges/game-of-two-stacks/problem)

```python
   not solved
```


2. [daily temperatures](https://leetcode.com/problems/daily-temperatures/)

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        for i in range(len(T) - 2, -1, -1):
            j = 1
            while T[i] >= T[i + j]:
                if not result[i + j]:
                    j = 0
                    break
                j += result[i + j]
            result[i] = j
        return result
```
## linklist questions

3. [remove duplicates from sorted list ii](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

```python
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
```





4. [remove duplicates from sorted list](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

>  1st method

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur=head
        if cur is None :
            return cur

        while cur.next :
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else :
                cur=cur.next
        return  head

```
 > 2nd method


```python
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
          le=len(temp)

          res=[0]*le
          stack=[le-1]

          for i in range(le-2, -1, -1):
              while stack and temp[stack[-1]]<=temp[i]:
                stack.pop()
              if stack:
                 res[i]=stack[-1]-i
              stack.append(i)


          return res

```
