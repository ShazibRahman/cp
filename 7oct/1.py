nums0=[1,2,3,4,5,6,7]
nums1=[-1,-100,3,99]
k0=3
k1=2
nums=nums1
k=k1

#actual code
def rotate(nums,k):
	for i in range(k):
		nums.insert(0,nums.pop())
	
#end of actual code
rotate(nums)
print(nums)
