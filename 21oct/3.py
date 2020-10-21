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
