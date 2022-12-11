def twoSum(nums, target):
        result_list = []
		#Two for loops for selecting two numbers and check sum equal to target or not
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
			#  j from i + 1; no need to check back elements it covers in i
			# Check sum == target or not
                if nums[i] + nums[j] == target:
                    result_list.append(i)
                    result_list.append(j)

        return result_list

def threeSum(nums):
    res = []        # Triples
    n = len(nums)   # Length of the list
    nums.sort()     # We need to sort the list first!
    
    for i in range(n-2):
        
        # Since the list is sorted, if nums[i] > 0, then all 
        # nums[j] with j > i are positive as well, and we cannot
        # have three positive numbers sum up to 0. Return immediately.
        if nums[i] > 0:
            break
            
        # The nums[i] == nums[i-1] condition helps us avoid duplicates.
        # E.g., given [-1, -1, 0, 0, 1], when i = 0, we see [-1, 0, 1]
        # works. Now at i = 1, since nums[1] == -1 == nums[0], we avoid
        # this iteration and thus avoid duplicates. The i > 0 condition
        # is to avoid negative index, i.e., when i = 0, nums[i-1] = nums[-1]
        # and you don't want to skip this iteration when nums[0] == nums[-1]
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        # Classic two pointer solution
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0: # sum too small, move left ptr
                l += 1
            elif s > 0: # sum too large, move right ptr
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                
                # we need to skip elements that are identical to our
                # current solution, otherwise we would have duplicated triples
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res

def fourSum(nums, target):
    def findNSum(nums, target, N, prefix, result):
        L = len(nums)
        if N == 2:
            l, r = 0, L-1
            while l < r:
                add = nums[l] + nums[r]
                if add == target:
                    result.append(prefix + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l-1] == nums[l]:
                        l += 1
                    while l<r and nums[r+1] == nums[r]:
                        r -= 1
                elif add > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in range(L-N+1):
                if target < N*nums[i] or target > N*nums[-1]: # key judgement
                    break
                if i == 0 or (i>0 and nums[i] != nums[i-1]):
                    findNSum(nums[i+1:], target-nums[i], N-1, prefix+[nums[i]], result)
        return

    nums.sort()
    res = []
    findNSum(nums, target, 4, [], res)
    return res