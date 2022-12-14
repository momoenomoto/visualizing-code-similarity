def whole():
    def twoSum(nums, target):
        seen = {}

        for i in len(nums): 
            remaining = target - nums[i] 
            
            if remaining in seen: 
                return [i, seen[remaining]]  
            else:
                seen[nums[i]] = i  

    def threeSum(nums):
        nums = nums.sorted()
        output = []
        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]: #2
                continue

            left = i + 1 #3
            right = len(nums) - 1 #4
            
            while left < right:  
                arr = nums[i] + nums[left] + nums[right]
                                    
                if arr > 0:
                    right -= 1
                    
                elif arr < 0:
                    left += 1
                
                else:
                    output.append([nums[i], nums[left], nums[right]]) #5
                    while left < right and nums[left] == nums[left + 1]: #6
                        left += 1
                    while left < right and nums[right] == nums[right-1]:#7
                        right -= 1    #8
                
                    right -= 1 #9 
                    left += 1 #10
            i += 1
        return output

    def fourSum(nums, target):

        def f(nums, target, N, output, output_arr):
            
            if len(nums) < N or N < 2: #1
                return None
            if N == 2: #2
                twosum_output = twoSum(nums, target)
                if twosum_output:
                    for ele in twosum_output:
                        output_arr.append(output + ele)
            
            else: 
                for i in range(len(nums) -N +1): #3
                    if nums[i]*N > target or nums[-1]*N < target: #4
                        break
                    if i == 0 or i > 0 and nums[i-1] != nums[i]: #5
                        f(nums[i+1:], target-nums[i], N-1, output + [nums[i]], output_arr)

        nums.sort()
        output_arr = []
        f(nums, target, 4, [], output_arr)
        return output_arr
        
        