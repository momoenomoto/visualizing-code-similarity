from collections import defaultdict

def twoSum(nums, target):
    seen = dict()
    
    for i, n in enumerate(nums):
        if target-n in seen:
            return [i,seen[target-n]]
        else:
            seen[n] = i
            
    # this place is unreachable
    return [0,0]

def threeSum(nums):
    Set=set()
    
    nums.sort()
    
    n=len(nums)
    for i in range(n):
        j=i+1
        k=n-1
        while(j<k):
            sum=nums[i]+nums[j]+nums[k]
            if sum==0:
                Set.add((nums[i],nums[j],nums[k]))
                k=k-1
                j=j+1
                    
            elif sum>0:
                k=k-1
                
            else:
                j=j+1
                
    return [list(i) for i in Set]

def fourSum(nums, target):
    res = set()

    def makeLegalPairs(list1, list2):
        for (i, j) in list1:
            for (k, l) in list2:
                if i!=k and i!=l and j!=k and j!=l:
                    new = sorted([nums[i], nums[j], nums[k], nums[l]])
                    res.add(tuple(new))

    helper = defaultdict(list)
    for index1 in range(len(nums)):
        for index2 in range(index1 + 1, len(nums)):
            helper[nums[index1] + nums[index2]].append((index1, index2))

    if not target and len(nums) >= 4 and nums[-1] == 0: return [[0,0,0,0]]
    save = set(helper.keys())
    for num in helper:
        tmp = target - num
        if tmp in save:
            makeLegalPairs(helper[num], helper[tmp])
    return res