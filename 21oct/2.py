class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        l,r=1,1
        for i in range(2,n):
            l,r=r,l+r
        return l+r
