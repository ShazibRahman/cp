class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l,r=cost[0],cost[1]
        for i in range(2,len(cost)):
            l,r=r,min(r,l)+cost[i]
        return min(l,r)
