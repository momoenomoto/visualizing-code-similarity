def whole():
    def longestPalindrome(s):

        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]

        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
        
    def trap(height):
        waterLevel = []
        left = 0
        for h in height:
            left = max(left, h) 
            waterLevel += [left] # over-fill it to left max height
        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height
        return sum(waterLevel)

    def minPathSum(grid):
        m, n = len(grid), len(grid[0])
        dp = [0] + [float("inf")] * (n-1)
        for i in range(m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                # minimum of row or column
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]

    def editDistance(word1, word2):
        m, n = len(word1), len(word2)  # switch word1 and word2 if m < n to ensure n ≤ m
        curr = list(range(n+1))
        for i in range(m):
            prev, curr = curr, [i+1] + [0] * n
            for j in range(n):
                curr[j+1] = prev[j] if word1[i] == word2[j] else min(curr[j], prev[j], prev[j+1]) + 1
        return curr[n]

    def longestValidParentheses(s):
        dp = [0 for x in range(len(s))]
        max_to_now = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: 
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now