def whole():
    def twoSum(nums, target):
        d={nums[0]:0}
        for i in range(1,len(nums)):
            rem=target-nums[i]
            if rem in d:
                return d[rem],i
            else:
                d[nums[i]]=i

    def threeSum(nums):
        nums.sort()
        ans = set()
        for i,v in enumerate(nums):
            twoSum(nums[i+1:],-v,ans)
        return ans

    def fourSum(nums, target):
        ans, n = [], len(nums)
        nums.sort()
        for a in range(n):
            for b in range(a+1, n):
                c = b+1; d = n-1
                while c<d:
                    sums = nums[a]+nums[b]+nums[c]+nums[d]
                    if sums < target: c += 1
                    elif sums > target: d -= 1
                    else:
                        to_append = [nums[a],nums[b],nums[c],nums[d]]
                        if to_append not in ans:
                            ans.append(to_append)
                        c +=1; d-=1
        return ans