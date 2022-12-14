def whole():
    def longestPalindrome(s):

        longest = ""
        grid = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            grid[i][i] = True
            longest = s[i]
            
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):  
                if s[i] == s[j]: 
                    if j-i ==1 or grid[i+1][j-1]:
                        grid[i][j] = True
                        if len(longest) < len(s[i:j+1]):
                            longest = s[i:j+1]
                
        return longest
        
    def trap(h):
        if len(h)<= 2:
            return 0
        res = 0
        i = 1
        j = len(h) - 1
        
        leftMax = h[0]
        rightMax = h[-1]
        
        while i <=j:
            if h[i] > leftMax:
                leftMax = h[i]
            if h[j] > rightMax:
                rightMax = h[j]
            
            if leftMax <= rightMax:
                res += leftMax - h[i]
                i += 1
                
            else:
                res += rightMax - h[j]
                j -= 1 
        return res

    def minPathSum(dp):
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j] + dp[i-1][j], dp[i][j] + dp[i][j-1])
                elif i > 0:
                    dp[i][j] += dp[i-1][j]
                elif j > 0:
                    dp[i][j] += dp[i][j-1]
            
        return dp[-1][-1]

    def editDistance(w1, w2):
        height, width = len(w1)+1, len(w2)+1
        prev = [i for i in range(width)]
        for i in range(1, height):
            curr = [i for _ in range(width)]
            for j in range(1, width):
                curr[j] = min(prev[j-1]+(w1[i-1] != w2[j-1]), prev[j]+1, curr[j-1]+1)
            prev = curr
        return prev[-1]

    def longestValidParentheses(s):
        maxL = 0
        stackk=[-1] 
        for i in range(len(s)):
            if s[i] == '(':
                stackk.append(i)
            else:
                stackk.pop()
                if not stackk: 
                    stackk.append(i)
                else:
                    maxL=max(maxL, i-stackk[-1])
        return maxL