class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_=nums[0]
        max_=nums[0]
        for i in range(1,len(nums)):
            sum_=max(sum_+nums[i],nums[i])
            max_=max(max_,sum_)
        return max_
