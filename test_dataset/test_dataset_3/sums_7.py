def twoSum(nums, target):
    nums = enumerate(nums)
    nums = sorted(nums, key=lambda x:x[1])
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l][1]+nums[r][1] == target:
            return sorted([nums[l][0]+1, nums[r][0]+1])
        elif nums[l][1]+nums[r][1] < target:
            l += 1
        else:
            r -= 1

def threeSum(nums):
    nums = sorted(nums)
    result = set()
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        target = 0 - nums[i]
        while l < r:
            if nums[l] + nums[r] == target:
                result.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return list(result)

def fourSum(nums, target):
    nums.sort()
    i = 0
    L = len(nums)
    res = []
    while i < L-3:
        j = i+1
        while j < L-2:
            left = j+1
            right = L-1
            new_target = target-nums[i]-nums[j]
            while left<right:
                if nums[left]+nums[right] > new_target:
                    right-=1
                elif nums[left]+nums[right] < new_target:
                    left+=1
                else:
                    res.append([nums[i],nums[j],nums[left],nums[right]])
                    temp_left = nums[left]
                    temp_right = nums[right]
                    while(left<right and nums[left]==temp_left):
                        left+=1
                    while(left<right and nums[right]==temp_right):
                        right-=1
            while j < L-3 and nums[j] == nums[j+1]:
                j+=1
            j+=1
        while i < L-4 and nums[i] == nums[i+1]:
            i+=1
        i+=1
    return res