class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1st solution
         return  len(nums)!=len(list(set(nums)))


        # 2nd solutin

         nums.sort()
         for i in range(len(nums)-1):
             if nums[i]==nums[i+1]:
                 return True
         return False

        #3rd solution
         dic={}
         for i in nums:
             if i in dic:
                 return True
             else:
                 dic[i]=1
         return False
