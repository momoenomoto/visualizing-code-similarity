def whole():
    def longestPalindrome(s):
        if len(s) < 2:
            return s
        start = 0
        maxLen = 1
        i = 0

        while i < len(s):
            l = i
            r = i
            while r < len(s) - 1 and s[r] == s[r+1]:
                r += 1
            i = r + 1
            while r < len(s)-1 and l > 0 and s[r+1] == s[l-1]:
                l -= 1
                r += 1
            if maxLen < r - l + 1:
                start = l
                maxLen = r - l + 1
        return s[start: start + maxLen]
        
    def trap(height):
            # left advances the left window, right advances the right window
        left, right = 0, len(height) - 1

        # left_max keeps track of the tallest height the left pointer has encountered,
        # right_max keeps track of the tallest height the right pointer has encountered,
        # and trapped_water keeps track of the number of units of trapped rain water
        left_max = right_max = trapped_water = 0
        
        while left < right:
            # get the current highest evelation on the left and right windows
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            # the smaller height side is the maximum amount of rain water that can be trapped
            # (otherwise we would incorrectly add water that would spill over the smaller height side),
            # so add the number of units of water trapped from the smaller height side
            if left_max <= right_max:
                # this will add the water trapped in height[left] relative to the tallest height we've seen on
                # the left side so far
                # if left_max was previously smaller than height[left], this will be 0
                trapped_water += left_max - height[left]
                left += 1
            else:
                trapped_wter += right_max - height[right]
                right -= 1
            
        return trapped_water

    def minPathSum(grid):
        m, n = len(grid), len(grid[0])
        memo = {}
        
        def dp(i, j):
            if i == m or j == n:
                return float("inf")
            
            if i == m-1 and j == n-1:
                return grid[i][j]
            
            key = (i, j)
            if key in memo:
                return memo[key]
            
            res = grid[i][j] + min(dp(i+1, j), dp(i, j+1))
            memo[key] = res
            return res
        
        return dp(0, 0)

    def editDistance(word1, word2):
        word1_len = len(word1)
        word2_len = len(word2)
        
        
        # When one of the strings is missing. the other one's length is required (either delete or insert)
        last_row = [0] * (word1_len+1)
            
        for c in range(word1_len - 1, -1, -1):
            last_row[c] = word1_len - c
        
        # Transitions
        for word2_p in range(word2_len - 1, -1, -1):
            cur_row = [0] * (word1_len+1)
            cur_row[word1_len] = word2_len - word2_p
            
            for word1_p in range(word1_len -1, -1, -1):
                if word1[word1_p] == word2[word2_p]:
                    cur_row[word1_p] = last_row[word1_p+1]
                else:
                    cur_row[word1_p] = 1 + min(
                        cur_row[word1_p+1], # delete
                        last_row[word1_p], # insert
                        last_row[word1_p+1] # replace
                    )
            
            last_row = cur_row

        return last_row[0]

    def longestValidParentheses(s):
        @functools.lru_cache(maxsize = None)
        def dp(s, i):
            if i < 0:
                return 0

            if s[i] == '(':
                return 0

            ans = 0
            length = dp(s, i - 1)
            if i - length - 1 >= 0 and s[i - length - 1] == '(':
                ans = length + 2 + dp(s, i - length - 1 - 1)

            max = max(max, ans)
            return ans

        for i in range(len(s)):
            dp(s, i)
            
        return max