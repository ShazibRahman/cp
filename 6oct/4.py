nums=[5,7,7,8,8,10]
target=5

def func(nums,target):
	l,r=-1,-1
	
	for i in range(len(nums)):
		if nums[i]==target:
			l=min(l,i) if l !=-1 else i
			r = max(r,i) 
	

			
	return [l,r]


print(func(nums,target))