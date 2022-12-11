def longestPalindrome(s):
    def expand_pallindrome(i,j):            
        while 0<=i<=j<n and s[i]==s[j]:
            i-=1
            j+=1                            
        return (i+1, j)

    n=len(s)
    res=(0,0)
    for i in range(n):
        b1 = expand_pallindrome(i,i)
        b2 = expand_pallindrome(i,i+1)            
        res=max(res, b1, b2,key=lambda x: x[1]-x[0]+1) # find max based on the length of the pallindrome strings.
                
    return s[res[0]:res[1]]
    
def trap(height):
    stack = []
    water = 0
    for i, e in enumerate(height):
        # we need to see if we can form a container
        while stack and e >= stack[-1][0]:
            popped, _ = stack.pop()
            # is it a container though? we have a left border?
            if stack:
                left_border, j = stack[-1]
                # we compute the water
                water += min(left_border-popped, e-popped)*(i-j-1)
        stack.append((e,i))
    return water

def minPathSum(grid):
    n = len(grid) # no of cells in each col
    m = len(grid[0]) # no of cells in each row

    # populate first row using m for no of cells in row
    for i in range(1,m):
        grid[0][i] = grid[0][i] + grid[0][i-1]

    # populate first col using n for no of cells in col
    for j in range(1,n):
        grid[j][0] = grid[j-1][0] + grid[j][0]

    # populate the rest
    for i in range(1,n):
        for j in range(1,m):
    	# get min seen so far plus curr cell value
            grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]

    # return last cell
    return grid[-1][-1]

def editDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(min(dp[i-1][j-1] + 1, dp[i-1][j] + 1), dp[i][j-1] + 1)
                    
    return dp[m][n]

def longestValidParentheses(s):
    stack, result = [(-1, ')')], 0
    for i, paren in enumerate(s):
        if paren == ')' and stack[-1][1] == '(':
            stack.pop()
            result = max(result, i - stack[-1][0])
        else:
            stack += (i, paren),
    return result