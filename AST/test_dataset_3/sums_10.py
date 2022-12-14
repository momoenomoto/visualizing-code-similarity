def whole():
    def twoSum(nums, target):
        complement ={}
        for i,v in enumerate(nums):
            # if v = nums[i] in complement, we find a solution
            if v in complement:
                return complement[v],i
            # if v = nums[i] not in complement, we store the compliment of the element into the dictionary.
            else:
                complement[target - v] = i
        return -1

    def threeSum(nums):
        nums.sort() # We sort nums first to more easily find duplicate numbers
        triplets = [] # We will store all the valid triplets in here
        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue # Skip duplicates
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1;
                    
                    # Skip all duplicates on left side
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    
                    # Skip all duplicates on right side
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif curSum < 0:
                    left += 1 # Our sum is too small, so we try to increase the sum
                else:
                    right -= 1 # Our sum is too big, so we try to decrease the sum
        return triplets

    def fourSum(nums, target):
        from collections import defaultdict
        dp = {}
        res = set()
        seen = defaultdict(list)
        # 1
        for r in range(len(nums)):
            for c in range(r):
                have = nums[r] + nums[c]
                need = target - have
                # 2
                if need in seen:
                    # 3
                    for r1,c1 in seen[need]:
                        if len({r1,c1,r,c}) == 4:
                            res.add( tuple(sorted([nums[r1],nums[c1],nums[r],nums[c]])) ) 
                seen[have].append((r, c))
        return res