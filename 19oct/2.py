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
