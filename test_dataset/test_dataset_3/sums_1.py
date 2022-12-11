def twoSum(nums, target):
    seen = {}
    for i, value in enumerate(nums): #1
        remaining = target - nums[i] #2
        
        if remaining in seen: #3
            return [i, seen[remaining]]  #4
        else:
            seen[value] = i  #5

def threeSum(nums):
    nums.sort()
    res = []

    for i in range(len(nums) -2): #1
        if i > 0 and nums[i] == nums[i-1]: #2
            continue
        left = i + 1 #3
        right = len(nums) - 1 #4
        
        while left < right:  
            temp = nums[i] + nums[left] + nums[right]
                                
            if temp > 0:
                right -= 1
                
            elif temp < 0:
                left += 1
            
            else:
                res.append([nums[i], nums[left], nums[right]]) #5
                while left < right and nums[left] == nums[left + 1]: #6
                    left += 1
                while left < right and nums[right] == nums[right-1]:#7
                    right -= 1    #8
            
                right -= 1 #9 
                left += 1 #10
    return res

def fourSum(nums, target):

    def helper(nums, target, N, res, results):
        
        if len(nums) < N or N < 2: #1
            return
        if N == 2: #2
            output_2sum = twoSum(nums, target)
            if output_2sum != []:
                for idx in output_2sum:
                    results.append(res + idx)
        
        else: 
            for i in range(len(nums) -N +1): #3
                if nums[i]*N > target or nums[-1]*N < target: #4
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]: #5
                    helper(nums[i+1:], target-nums[i], N-1, res + [nums[i]], results)

    nums.sort()
    results = []
    helper(nums, target, 4, [], results)
    return results
    
    