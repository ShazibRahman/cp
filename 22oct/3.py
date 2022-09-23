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
