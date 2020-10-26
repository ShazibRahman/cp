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
def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            try:
                dic[nums[i]].append(i)
            except:
                dic[nums[i]]=[i]
        print(dic)
        for i in range(len(nums)):
            c = target-nums[i]

            try:
                if c in dic.keys():
                    if c==nums[i] and len(dic[c])>1:
                        return dic[c][:2]
                    elif c!=nums[i]:
                        return [i,dic[c][0]]
            except:
                pass
