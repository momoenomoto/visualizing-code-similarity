def whole():
    def longestPalindrome(s):
        def expand_center(i,j):            
            while 0<=i<=j<n and s[i]==s[j]:
                i-=1
                j+=1                
            
            return (i+1, j)  

        n=len(s)
        res=max([expand_center(i,i+offset) for i in range(n) for offset in range(2)], key=lambda x: x[1]-x[0]+1)
                    
        return s[res[0]:res[1]]
        
    def trap(height):
        if height == []: return 0

        n = len(height)
        max_l = max_r = [0]* n
        max_l[0] = max_r[n-2] = 0
        i = 1
        while i < n:
            max_l[i] = max(max_l[i - 1], height[i-1])
            i += 1
            
        i = n - 2
        while i > -1:
            max_r[i] = max(max_r[i + 1], height[i + 1])
            i -= 1

        res = 0
        i = 0
        while i < n:
            
            lower = min(max_l[i], max_r[i])
            
            max_i = lower - height[i]
            
            if max_i > 0:
                res += max_i

            i+=1
                
        return res

    def minPathSum(grid):
        i = 1
        while i < len(grid[0]):
            grid[0][i] += grid[0][i-1]
            i += 1

        i = 1
        # left most col
        while i < len(grid): 
            grid[i][0] += grid[i-1][0]
            i += 1

        i = 1
        while i < len(grid): 
            j = 1
            while j < len(grid[0]):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]) 
                j += 1
            i += 1

        targetX, targetY = len(grid)-1, len(grid[0])-1
        return grid[targetX][targetY]

    def editDistance(word1, word2):
        n = len(word1); m = len(word2)
        
        grid = [[0]*(m+1) for _ in range(n+1)]
        
        j = 0
        while j < m+1:
            grid[0][j] = j
            j += 1
        
        i = 0
        while i < n+1:
            grid[i][0] = i
            i += 1
        
        i = 1
        while i < n+1:
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    grid[i][j] = grid[i-1][j-1]
                else:
                    grid[i][j] = 1 + min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1])
            i += 1
        
        return grid[-1][-1]

    def longestValidptheses(s):
        stk, res = [(-1, ')')], 0
        for i, p in enumerate(s):
            if p == ')' and stk[-1][1] == '(':
                stk.pop()
                res = max(res, i - stk[-1][0])
            else: stk += (i, p),
        return res