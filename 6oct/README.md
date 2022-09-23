# 6 october (Leetcode)


1. [Two sum](https://leetcode.com/problems/two-sum/)

```python
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

```
2. [Remove duplicates from sorted array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for n in range(1, len(nums)):
            if nums[n] != nums[n - 1]:
                nums[i] = nums[n]
                i += 1
        return i

```
3. [Find first and last position of element in sorted array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

```python
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
```
4. [Best time to buy and sell stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```python

```
