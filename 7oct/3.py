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
