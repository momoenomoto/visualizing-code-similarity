def longestPalindrome(s):

    def helper(s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]

    res = ''
    for i in range(len(s)):
        res = max(res, helper(s, i, i), helper(s, i, i+1), key=len)
    return res
    
def trap(bars):
    if not bars or len(bars) < 3:
        return 0
    volume = 0
    left, right = 0, len(bars) - 1
    l_max, r_max = bars[left], bars[right]
    while left < right:
        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
        if l_max <= r_max:
            volume += l_max - bars[left]
            left += 1
        else:
            volume += r_max - bars[right]
            right -= 1
    return volume

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]

def editDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [list(range(n+1))]+[[r+1]+[0]*n for r in range(m)]
    for i in range(m):
        for j in range(n):
            dp[i+1][j+1] = dp[i][j] if word1[i]==word2[j] else min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
    return dp[m][n]

def longestValidParentheses(s):
    stack, maxLen = [(")", -1)], 0
        
    for i in range(len(s)):
        if s[i] == ")" and stack[-1][0] == "(":
            stack.pop()
            maxLen = max(maxLen, i-stack[-1][1])
        else:
            stack.append((s[i], i))
    return maxLen