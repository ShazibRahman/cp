# 12 oct Leetcode

1. [Valid paranthesis](https://leetcode.com/problems/valid-parentheses/)

```python
char_stack=[]
mapper={"(":")","[":"]","{":"}"}

def func(a):
  for char in a:
    if char in mapper:
       char_stack.append(char)
    else:
       if not char_stack or mapper[char_stack.pop()]!=char:
          return False
  return not char_stack

print(func('[{}]'))


```

2. [min-stack](https://leetcode.com/problems/min-stack/)

```python
class MinStack:

    def __init__(self):
        self.st=[]
        self.minimun=None

        """
        initialize your data structure here.
        """


    def push(self, x: int) -> None:
        self.st.append(x)
        self.minimun=min(self.st) if self.st else None


    def pop(self) -> None:
        self.st.pop()
        self.minimun=min(self.st) if self.st else None


    def top(self) -> int:
         return self.st[-1]


    def getMin(self) -> int:
        return self.minimun

```
3. [remove all adajcent duplicates in strings](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
          stack=[]
          for i in s:

            if stack and i == stack[-1] :
                stack.pop()
            else:
                stack.append(i)
          return "".join(stack)


```
4. [decode string](https://leetcode.com/problems/decode-string/)

```python
class Solution:
    def decodeString(self, s: str) -> str:

        num_stack, num = [], 0
        str_stack = ['']
        for char in s:
            if char == "[":
                num_stack.append(num)
                str_stack.append('')
                num = 0
            elif char == "]":
                decoding = num_stack.pop() * str_stack.pop()
                str_stack[-1] += decoding
            elif char.isdigit():
                num = num * 10 + int(char)
            else:
                str_stack[-1] += char

        return str_stack[-1]

```
