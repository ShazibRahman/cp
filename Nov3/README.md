# 3 Nov (leetcode) [Day 15]

## Based on two pointers

---


## 1.  [Boats to save people](https://leetcode.com/problems/boats-to-save-people/)

> * In order to solve these type of questions where two of same Array / list are to be matched . we use two pointers concept.
> * So to solve the questions, we have to sort the Array in Decreasing order . this will help to optimize the solution.
> * after sorting take two pointers , say __i__ and __j__   and initilize them to 0 index and second one to last index.
> * Now iterate the list till condition __i__ <= __j__ .
> * Now look if weight at those index is either small or  equal to the limit . If __YES__ we decrement the value of j and  if __NO__ we dont decrement the value of j.
> * Array is sorted in decreasing ordern. and if the condition doesn't match . then we know that both can't go in same boat . and the weighted person is at __ith__ index cause we have sorted the array  and not Decreasing the __jth__ state that the only the weighted of them  __ith__ have crossed the river .
> * if the condition was satisfied both the __i__ and __j__ would have crossed and we have increase the ith and decreased the jth value.
> * then no matter whether the above case is matched , we increase __ith__ position along with the total count variable  by 1 .

> * and return the total count at last.

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse= True)
        count=0
        i,j=0,len(people)-1
        while i <= j:
            if (people[i]+people[j] <= limit):
                j-=1
            count+=1
            i+=1
        return count

```
---


## 2. [Longest Mountains in an Array](https://leetcode.com/problems/longest-mountain-in-array/)

> * Filtering out the peaks.
> * checking the left side using a while loop if it satisfies up until it doesn't and point at using a pointer variable. We do that two variables away from the peak at a time from the left then we move the pointer one step to the left.
> * checking the right side using a while loop if it satisfies up until it doesn't and point at using a pointer. variable. We do that two variables at a time from the right we move the pointer one step to the right.
> * Now that you have two pointers, one on the left and one on the right. subtract them out to see the actual value. and then take out one, [ peak ].
> * Compare it to the current maximum longest peak. and choose the higher one.
> *  Move the pointer all the way to the right pointer of the last while loop. WHY?, because you already explored the variables before that. so it does not make sense to explore these values again.
> * Then return the answer

```python
class Solution:
    def longestMountain(self, a: List[int]) -> int:
        longestpeak=0
        i=1
        while i < len(a)-1:
            if a[i]>a[i-1] and a[i]> a[i+1]:
                pass
            else:
                i+=1
                continue
            left=i-2
            while left >= 0 and a[left] < a[left+1]:
                left-=1

            right=i+2

            while right< len(a) and a[right-1] > a[right]:
                right+=1
            peak=right -left -1

            longestpeak=max(longestpeak,peak)
            i=right
        return longestpeak

```
