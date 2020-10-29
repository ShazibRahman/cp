# 22 october (Leetcode)

1. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        le=len(s)
        st,end=0,0
        dp=[[False]*le for x in range(le)]
        for g in range(le):

            for  i,j in enumerate (range(g,le)):
                if g==0:
                    dp[i][j]=True
                elif g==1:
                    if (s[i]==s[j]):
                         dp[i][j]= True



                else :
                      if (s[i]==s[j]) and dp[i+1][j-1]:
                            dp[i][j]=True

                if dp[i][j]:
                    st,end=i,j

        return  s[st:end+1]
```

2. [Unique Path 2](https://leetcode.com/problems/unique-paths-ii/)

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]:
            return 0
        obstacleGrid[0][0]=1
        for i in range(1,n):
            obstacleGrid[0][i]=obstacleGrid[0][i]==0 and obstacleGrid[0][i-1]==1
        for i in range(1,m):
            obstacleGrid[i][0]=obstacleGrid[i][0]==0 and obstacleGrid[i-1][0]==1


        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j]=0
        return int(obstacleGrid[-1][-1])
```

3. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1 :
            return 0
        min_=prices[0]
        max_=0
        for i in range(len(prices)):
            min_=min(min_,prices[i])
            max_=max(max_,prices[i]-min_)
        return max_
```

4. [Is Subsequence](https://leetcode.com/problems/is-subsequence/)

```python
class Solution:
    def isSubsequence(self, s: str, t: str) :
        i,j,le1,le2=0,0,len(s),len(t)
        while i< le1 and j<le2:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return le1==i
```
