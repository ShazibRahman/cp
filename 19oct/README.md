# 19 october (Leetcode)

1. [maximum problems of two elements in an array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array)

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_=0
        left=0
        right=len(nums)-1
        while left < right:
            max_=max   ((nums[left]-1)*(nums[right]-1), max_)
            if nums[left]>nums[right]:
                right-=1
            else:
                left+=1
        return max_
```

2. [median of two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=nums1+nums2
        nums1.sort()
        if len(nums1)%2==0:
            med=len(nums1)//2
            return (nums1[med-1]+nums1[med])/2
        else:
            med=len(nums1)//2
            return  nums1[med]
```


3. [unique paths](https://leetcode.com/problems/unique-paths/)

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix=[[0]*n]*m
        for i in range(m):
            for j in range(n):
                if (i==0 or  j==0):
                    matrix[i][j]=1
                else :
                    matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]

        return matrix[m-1][n-1]
```


4. [two sum ii input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        while l <r:
            if nums[l]+nums[r]==target:
                return [l+1,r+1]
            elif nums[l]+nums[r]> target:
                r-=1
            else:
                l+=1
```
