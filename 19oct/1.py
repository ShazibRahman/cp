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
