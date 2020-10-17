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
# 2nd solutions using stack
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
