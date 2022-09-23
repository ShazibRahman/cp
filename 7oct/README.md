1. [Rotate array](https://leetcode.com/problems/rotate-array/)

```python
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
```
2. [Can place flowers](https://leetcode.com/problems/can-place-flowers/)

```python
flowerbed=[1,0,0,0,1]
n=2

def flow(flowerbed,n):
	le=len(flowerbed)
	if le==1:
		return True if n<=0 or flowerbed[0]==0 else False
	rem=n

	for i in range(le):
		if flowerbed[i]==1:
			continue
		elif (i==0 and flowerbed[i+1]==0) or (i==le-1 and flowerbed[i-1]==0) or (flowerbed[i-1]==0 and flowerbed[i+1]==0):
			flowerbed[i]=1
			rem-=1
			print(flowerbed,rem)
	return rem<=0



print(flow(flowerbed,n))
```
3. [Container with most water](https://leetcode.com/problems/container-with-most-water/)

```python
height=[1,8,6,2,5,4,8,3,7]
def max_area(height):

  max_=0
  le=len(height)
  left,right=0,le-1
  while left < right:


       k=min(height[left],height[right])*(right-left)

       if  k>max_:
          max_=k
       if height[left]>height[right]:
           right-=1
       else:
          left+=1

  return max_

print(max_area(height))
```
4. [Word serach](https://leetcode.com/problems/word-search/)

```python
not solved
```
