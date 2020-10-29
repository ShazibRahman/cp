# 14 october (Hackerrank)

## array
1. [kangaroo](https://www.hackerrank.com/challenges/kangaroo/problem)

```python
def kangaroo(x1, v1, x2, v2):
    if (x1>x2 and v1>v2) or(x2>x1 and v2>v1)  :
        return 'NO'
    if v1>v2:
        while x1<x2:
            x1+=v1
            x2+=v2
        if x1==x2:
            return "YES"
    if v2> v1:
        while x2<x1:
            x1+=v1
            x2+=v2
        if x1==x2:
            return 'YES'
    return 'NO'
```

2. [climbing-the-leaderboard](https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem)
```python
def func(ranked , player):
  out=[]
  ranked=list(set(ranked))
  ranked.sort(reverse=True)


  i=0
  while i < len(player):
     while ranked and ranked[-1]<= player[i]:
       ranked.pop()

     if not ranked:
        out.append(1)
     else:
        out.append(len(ranked)+1)
     i+=1

  return out


```



## linked list

3. [reverse a doubly linked list](https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem)
```python
def reverse(head):


    while head :
        nex=head.next
        head.next,head.prev=head.prev,head.next
        prev=head
        head=nex



    return prev
```


4. [detect whether a linked list contains a cycle](https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem)
```python
def has_cycle(head):
    fast=slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
                return True
    return False
```
