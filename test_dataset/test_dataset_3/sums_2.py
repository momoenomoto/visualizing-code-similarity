def twoSum(nums, target):
    tmp = {}
    for i, num in enumerate(nums):
        if target - num in tmp:
            return [tmp[target - num], i]
    tmp[num] = i
    return [-1, -1]

def threeSum(nums):
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res

def fourSum(nums, target):
    import collections, itertools
    two_sum = collections.defaultdict(list)
    res = set()
    for (n1, i1), (n2, i2) in itertools.combinations(enumerate(nums), 2):
        two_sum[i1+i2].append({n1, n2})
    for t in list(two_sum.keys()):
        if not two_sum[target-t]:
            continue
        for pair1 in two_sum[t]:
            for pair2 in two_sum[target-t]:
                if pair1.isdisjoint(pair2):
                    res.add(tuple(sorted(nums[i] for i in pair1 | pair2)))
        del two_sum[t]
    return [list(r) for r in res]