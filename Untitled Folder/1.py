def jump(nums) -> int:

        le=len(nums)
        ju=[0]*le
        for i in range(le-2,-1,-1):
                if nums[i]==0:
                   ju[i]=ju[i+1]
                   continue
                ju[i]=min(ju[i+1:i+nums[i]+1])+1
                print(ju)
        return ju[0]


#2nd and far  better than my solution


        n = len(nums)
        if n < 2:
            return 0

        steps = 1
        max_reach = nums[0]
        next_check = nums[0]



        for index, val in enumerate(nums):


            if index > next_check:
                steps += 1
                next_check = max_reach
            max_reach = max(max_reach, index+val)


        return steps #+ 1 if not index
