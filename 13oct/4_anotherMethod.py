class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
          le=len(temp)

          res=[0]*le
          stack=[le-1]

          for i in range(le-2, -1, -1):
            if stack and temp[stack[-1]]> temp[i]:
              res[i]=stack[-1]-i
              stack.append(i)

            else:
              while stack and temp[stack[-1]]<=temp[i]:
                stack.pop()
              if stack:
                 res[i]=stack[-1]-i
              stack.append(i)


          return res
