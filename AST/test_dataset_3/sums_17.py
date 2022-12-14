def whole():
    from collections import defaultdict, Counter

    def twoSum(nums, target):
        # Brute force
            
        for index, num in enumerate(nums):
            for other_index, other_num in enumerate(nums):
                if num + other_num == target and index != other_index:
                    return [index, other_index]
                
        # Two pass hash table
        
        hash_table = {n: i for i, n in enumerate(nums)}
        # Creates a hash table with each number and their indexes
        for i, n in enumerate(nums):
            complement = target - n # Gets the complement of the number
            if complement in hash_table.keys() and hash_table[complement] != i:
                # Check if the complement is in the hash table
                return [i, hash_table[complement]]
                # Returns the index and the index of the complement
                
                
        # One pass hash table
        
        hash_table = {}
        # Creates the hash table
        for i, n in enumerate(nums):
            complement = target - n
            # Gets the complement
            if complement in hash_table.keys():
                # Check if the complement exists, then returns
                return [i, hash_table[complement]]
            hash_table[n] = i
            # Otherwise it adds the number and index to the hash table

    def threeSum(nums):
        counter = Counter(nums)
        nums = sorted(counter)
        ret = []
        for i, num in enumerate(nums):
            # case i. three numbers are the same - [0,0,0]
            if num==0:
                if counter[num] > 2:
                    ret.append([0, 0, 0])
            # case ii. two numbers are the same
            elif counter[num] > 1 and -2 * num in counter:
                ret.append([num, num, -2 * num])
            # case iii. not any of the three numbers are the same
            if num < 0:
                opposite = -num
                left = bisect_left(nums, opposite - nums[-1], i + 1)
                right = bisect_right(nums, opposite / 2, left)
                for a in nums[left:right]:
                    b = opposite - a
                    if b in counter and a!=b:
                        ret.append([num, a, b])
        return ret

    def fourSum(nums, target):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                diff = target - nums[i]
                threeSums = threeSum(nums[i+1:], diff)
                for threeSum in threeSums:
                    res.append([nums[i]] + threeSum)
        return res