# 17 october (leetcode)

1. [plus one](https://leetcode.com/problems/plus-one/)

```python
class Solution:
    def plusOne(self, a: List[int]) -> List[int]:
        b=[]
        carry,f=0,0
        while a:

            if f==0 :
                b.insert(0,((a[-1]+1)%10))
                carry=(a.pop()+1)//10
                f+=1
            else:
                b.insert(0,(a[-1]+carry)%10)
                carry=(a.pop()+carry)//10

        if  carry:
            b.insert(0,carry)
        return b
```


2. [number of students doing homework at a given time](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/)

```python
class Solution:
    def busyStudent(self, a: List[int], b: List[int], c: int) -> int:
        i=0
        while a and b:
            if c>=a[-1] and c<=b[-1]:

                i+=1
            a.pop()
            b.pop()
        return i
```



3. [trapping rain water](https://leetcode.com/problems/trapping-rain-water)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
#         1st solution using dynamic programming
         if not height:
             return 0
         total=0
         le=len(height)
         right=[0]*le
         left=[0]*le
         left[0]=height[0]
         right[-1]=height[-1]
         for i in range(1,le):
             left[i]=max(height[i],left[i-1])



         for i in range(le-2,-1,-1):
             right[i]=max(height[i],right[i+1])


         for i in range(1,le):
             total+=min(left[i],right[i])-height[i]


         return total
```
> 2nd solutions using stack
```python

        st=[]
        total=0
        current=0
        while current <len(height):
            while st and height[current]> height[st[-1]]:
                top=st[-1]
                st.pop()
                if not st:
                    break
                distance=current-st[-1]-1
                bounded_height=min(height[current],height[st[-1]])-height[top];
                total+=distance*bounded_height

            st.append(current)
            current+=1
        return total
```


4. [contains-duplicate](https://leetcode.com/problems/contains-duplicate)

```python
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
```
