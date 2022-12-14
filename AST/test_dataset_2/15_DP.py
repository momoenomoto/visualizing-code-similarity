def whole():
    def longestPalindrome(s):
        res = ""
        length = len(s)
        def helper(left: int, right: int):
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
                
            return s[left + 1 : right]
        
        
        for index in range(len(s)):
            res = max(helper(index, index), helper(index, index + 1), res, key = len)
            
        return res
        
    def trap(height):
        max_left = max_right = 0
        left, right = 0, len(height) - 1

        total = 0
        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if height[left] <= height[right]:
                total += max_left - height[left]
                left += 1
            else:
                total += max_right - height[right]
                right -= 1
        return total

    def minPathSum(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(i+j==0):
                    continue
                if(i*j!=0):
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
                elif(i==0):
                    grid[i][j]+=grid[i][j-1]
                elif(j==0):
                    grid[i][j]+=grid[i-1][j]                
        return(grid[-1][-1])

    def editDistance(word1, word2):
        def f(self,i,j,s,t,dp):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==t[j]:
                dp[i][j]= 0 + self.f(i-1,j-1,s,t,dp)
            else:
                dp[i][j]= min((1+self.f(i-1,j,s,t,dp)),(1+self.f(i,j-1,s,t,dp)),(1+self.f(i-1,j-1,s,t,dp)))
            return dp[i][j]
            
        m=len(word1)
        n=len(word2)
        dp=[[-1 for i in range(n)]for j in range(m)]
        return f(m-1,n-1,word1,word2,dp)

    def longestValidParentheses(s):
        if not s:
            return 0
        stack = [-1] # 
        max_len = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    curr_len = i - stack[len(stack)-1]
                    max_len = max(curr_len, max_len)
        return max_len