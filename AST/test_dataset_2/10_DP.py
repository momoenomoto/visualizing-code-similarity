def whole():
    def longestPalindrome(s):
        if len(s) < 2: 
            return s[0] if s else ''
        dp = [[False] * len(s) for _ in range(len(s))]
        max_seen = 1
        mv = s[0]
        for i in range(len(s)):
            for j in range(i):
                if s[i] == s[j] and ((i-j+1) <= 3 or dp[i-1][j+1]):
                    dp[i][j] = True
                    if i-j+1 >= max_seen:
                        max_seen = i-j+1
                        mv = s[j:i+1]

        return mv
        
    def trap(height):
        left = 0
        right = len(height) - 1
        left_max = right_max = water = 0
        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
                
        return water

    def minPathSum(grid):
        memo = {}
        def recurse(i,j):
            if (i,j) == (len(grid)-1, len(grid[0])-1): # reachedt traget
                return grid[i][j] # return the value of the cell to be added to the sum     
            if i > len(grid)-1 or j > len(grid[0])-1: # out of bounds
                return float('inf') # return a huge number to cause the path to be disgarded        
            if (i,j) in memo:
                return memo[(i,j)]      

            result = grid[i][j] + min(recurse(i+1, j), recurse(i, j+1))
            memo[(i,j)] = result
            return result

        return recurse(0,0) # starting Node

    def editDistance(word1, word2):
        edits = [[x for x in range(len(word1) + 1)] for y in range(len(word2) + 1)] #initialize 2d
        for i in range(1, len(word2) + 1): #initailize first column(012345)
            edits[i][0] = edits[i - 1][0] + 1
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word2[i - 1] == word1[j - 1]: #if same just check diaginal
                    edits[i][j] = edits[i - 1][j - 1]
                else:
                    edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i][j - 1], edits[i - 1][j]) #check all three vals, find min and add 1
        return edits[-1][-1] #return final val of our 2d matrix(last row last col)

    def longestValidParentheses(s):
        stack = [-1]
        
        max_length = 0
        
        # linear scan each index and character in input string s
        for cur_idx, char in enumerate(s):
            
            if char == '(':
                
                # push when current char is (
                stack.append( cur_idx )
                
            else:
                
                # pop when current char is )
                stack.pop()
                
                if not stack:
                    
                    # stack is empty, push current index into stack
                    stack.append( cur_idx )
                else:
                    # stack is non-empty, update maximal valid parentheses length
                    max_length = max(max_length, cur_idx - stack[-1])
                
        return max_length