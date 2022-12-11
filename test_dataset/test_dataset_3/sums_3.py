def twoSum(nums, target):
    map = {}
    for i in range(len(nums)):
        if nums[i] not in map:
            map[target - nums[i]] = i + 1
        else:
            return map[nums[i]], i + 1

    return -1, -1

def threeSum(nums):
    res = set()

	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(nums)
        elif num < 0: 
            n.append(nums)
        else:
            z.append(nums)

	#2. Create a separate set for negatives and positives for O(1) look-up times
    N, P = set(n), set(p)

	#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	#   i.e. (-3, 0, 3) = 0
    if z:
        for num in P:
            if -1*num in N:
                res.add((-1*num, 0, nums))

	#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
    if len(z) >= 3:
        res.add((0,0,0))

	#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            target = -1*(n[i]+n[j])
            if target in P:
                res.add(tuple(sorted([n[i],n[j],target])))

	#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            target = -1*(p[i]+p[j])
            if target in N:
                res.add(tuple(sorted([p[i],p[j],target])))

    return res

def fourSum(nums, target):
    nums.sort()
    result = []
    for i in xrange(len(nums)-3):
        if nums[i] > target/4.0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target2 = target - nums[i]
        for j in xrange(i+1, len(nums)-2):
            if nums[j] > target2/3.0:
                break
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            l = len(nums) - 1
            target3 = target2 - nums[j]
            # we should use continue not break
            # because target3 changes as j changes
            if nums[k] > target3/2.0:
                continue
            if nums[l] < target3/2.0:
                continue
            while k < l:
                sum_value = nums[k] + nums[l]
                if sum_value == target3:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    kk = nums[k]
                    k += 1
                    while k<l and nums[k] == kk:
                        k += 1
                    
                    ll = nums[l]
                    l -= 1
                    while k<l and nums[l] == ll:
                        l -= 1
                elif sum_value < target3:
                    k += 1
                else:
                    l -= 1
    return result