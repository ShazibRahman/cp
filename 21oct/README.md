# 21 october (Leetcode)


1. [Maximum subarray](https://leetcode.com/problems/maximum-subarray/)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_=nums[0]
        max_=nums[0]
        for i in range(1,len(nums)):
            sum_=max(sum_+nums[i],nums[i])
            max_=max(max_,sum_)
        return max_
```
#21 october (Leetcode)

2. [Climbing stairs](https://leetcode.com/problems/climbing-stairs/)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        l,r=1,1
        for i in range(2,n):
            l,r=r,l+r
        return l+r
```

3. [House robber](https://leetcode.com/problems/house-robber/)

```python
class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        l,mid,r=nums[0],nums[1],nums[0]+nums[2]

        for i in range(3,len(nums)):
            l,mid,r=mid,r,max(l,mid)+nums[i]
        return max(mid,r)
```

4. [Longest valid parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        max_=0
        for i in range(len(s)):
            if s[i]=="(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    max_=max(max_,i-st[-1])
        return max_
```
