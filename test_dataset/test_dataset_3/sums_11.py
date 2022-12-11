def twoSum(nums, target):
    memo = {}
    for idx, ele in enumerate(nums):
        if target - ele in memo:
            return [memo[target - ele], idx]
        memo[ele] = idx

def threeSum(nums):
    result = set([])
    add = sorted([n for n in nums if n>0])
    add_c = set(add)
    zeros = [n for n in nums if n == 0]
    subtract = sorted([n for n in nums if n<0])
    subtract_c = set(subtract)
    # all zeros
    if len(zeros)>2:
        result.add((0,0,0))
    # add zeros subtract
    if len(zeros)>0:
        for n in subtract:
            if -n in add_c:
                result.add((n,0,-n))
    # add subtract subtract
    n = len(subtract)
    for i in range(n):
        for j in range(i+1,n):
            difference = -(subtract[i]+subtract[j])
            if difference in add_c:
                result.add((subtract[i],subtract[j],difference))
    # add add subtract
    n = len(add)
    for i in range(n):
        for j in range(i+1,n):
            difference = -(add[i]+add[j])
            if difference in subtract_c:
                result.add((difference,add[i],add[j]))
    return list(result)

def fourSum(nums, target):
    nums.sort()
    result = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            # two sum problem solution
            new_target = target - (nums[i] + nums[j])
            start = j+1
            end = n-1
            while end > start:
                if(nums[start] + nums[end] == new_target):
                    result.add((nums[i], nums[j], nums[start], nums[end]))
                    end -= 1
                    start += 1
                elif nums[start] + nums[end] > new_target:
                    end -= 1
                else:
                    start += 1
    return result