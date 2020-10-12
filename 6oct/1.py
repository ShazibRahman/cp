'''
practise code
arr=[3,3]
target=6

def func(arr, tar):
	le=len(arr)
	for i in range(le):
		for j in range(i+1,le):
			if arr[i]+arr[j]==target:
				return [i,j]


print(func(arr,target))

'''

# actual code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        le=len(nums)
        for i in range(le):
            for j in range(i+1,le):
                if nums[i]+nums[j]==target:
                    return [i,j]
        