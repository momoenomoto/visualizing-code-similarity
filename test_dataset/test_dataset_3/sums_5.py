def twoSum(nums, target):
    mem = {}
    for i, value in enumerate(nums): #1
        left = target - nums[i] #2
        
        if left in mem: #3
            return [i, mem[left]]  #4
        else:
            mem[value] = i  #5

def threeSum(nums):
    res = []
    nums.sort()
    
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        res_2sum = twoSum(nums[i+1:], -nums[i])
        if res_2sum ==[]:
            continue
        else:
            for index in res_2sum:
                instance = index+[nums[i]]
                res.append(instance)
    
    output = []
    for index in res:
        if index not in output:
            output.append(index)
        
    return output

def fourSum(nums, target):

    def helper_f(nums, target, N, res, results):
        
        if len(nums) < N or N < 2: #1
            return
        if N == 2: #2
            res_2sum = twoSum(nums, target)
            if res_2sum != []:
                for index in res_2sum:
                    results.append(res + index)
        
        else: 
            for i in range(len(nums) -N +1): #3
                if nums[i]*N > target or nums[-1]*N < target: #4
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]: #5
                    helper_f(nums[i+1:], target-nums[i], N-1, res + [nums[i]], results)

    nums.sort()
    results = []
    helper_f(nums, target, 4, [], results)
    return results
    
    