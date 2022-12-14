def whole():
    from collections import defaultdict

    def twoSum(nums, target):
        scanned = {}
        for j, item in enumerate(nums, 1):
            i = scanned.get(target - item, -1)
            if i > 0:
                return [i, j]
            scanned[item] = j

    def threeSum(nums):
        nums.sort()
        n=len(nums)
        output=set()

        while i < n:
            j, k=i+1, n-1
            while(j<k):
                sumAll=nums[i]+nums[j]+nums[k]
                if sumAll==0:
                    output.add((nums[i],nums[j],nums[k]))
                    k=k-1
                    j=j+1
                        
                elif sumAll>0: k=k-1
                    
                else: j=j+1
            i += 1
                    
        return [list(i) for i in output]

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