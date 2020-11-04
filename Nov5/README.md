#  5 Nov (leetcode) [Day 16]

---

## 1. [Move Zeroes](https://leetcode.com/problems/move-zeroes/)

> * first replace all zeroes with the next none zero values and then add the 0 values to the last.

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last]=nums[i]
                last+=1
        for i in range(last,len(nums)):
            nums[i]=0

```

## 2. [Sort Colors](https://leetcode.com/problems/sort-colors/submissions/)

> * Use any Sorting technique simple

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last]=nums[i]
                last+=1
        for i in range(last,len(nums)):
            nums[i]=0

```
