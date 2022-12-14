def whole():
    def twoSum(nums, target):
        elements = dict()
        
        for index, value in enumerate(nums):
            ans = target- value
            #ans = the one we are searching 
            # we are keeping all the elements on dict called elements to check whether we have seen the ans value before by using dic
            
            if ans in elements:
                return [elements[ans], index]
            
            #adding current value to dic if ans is not in the elements we have seen before
            elements[value] = index
        
        #we are returning empty list 
        return []

    def threeSum(nums):
        if len(nums) <3: # deal with special input
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]


        nums = sorted(nums) # sorted, O(nlgn)
        ans = []

        for i in range(len(nums) -2):
            j = i+1
            k = len(nums) -1 # hence i < j < k

            while j<k: # if not cross line
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum == 0:
                    ans.append((nums[i], nums[j], nums[k]))

                if temp_sum > 0: # which means we need smaller sum, move k backward, remember we sort the array
                    k -= 1
                else:
                    j += 1

        return list(set(tuple(ans)))

    def fourSum(nums, target):
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[left] + nums[right]+nums[j]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        ans.add(tuple(sorted((nums[i], nums[left], nums[right],nums[j]))))
                    
                        left += 1
                        right -= 1
        return ans