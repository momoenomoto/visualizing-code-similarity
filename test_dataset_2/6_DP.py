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
    if height == []:
        return 0

    n = len(height)
    max_left = [0]* n
    max_right = [0]* n
    ##print(max_left, height)
    max_left[0] = 0
    max_right[n-1] = 0
    for i in range (1, n):
        max_left[i] = max(max_left[i - 1], height[i-1])
         
    for i in range(n-2, -1, -1):
       
        max_right[i] = max(max_right[i + 1], height[i + 1])

    output = 0
    print(max_left, max_right)
    
    for i in range(n):
	    
        lower_boundary = min(max_left[i], max_right[i])
        
        max_trap_at_i = lower_boundary - height[i]
        
        if max_trap_at_i > 0:
            output += max_trap_at_i
            
    return output

def minPathSum(grid):
    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i-1]

	# left most col
    for i in range(1, len(grid)):
        grid[i][0] += grid[i-1][0]

	# rest of the grid
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1]) 

    trgtX, trgtY = len(grid)-1, len(grid[0])-1
    return grid[trgtX][trgtY]

def editDistance(w1, w2):
    n = len(w1); m = len(w2)
    
    dp = [[0]*(m+1) for i in range(n+1)]
    
    for j in range(m+1): # Base Case 0th row where len(w1) = 0
        dp[0][j] = j
    
    for i in range(n+1): # Base Case 0th column where len(w2) = 0
        dp[i][0] = i
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                                    dp[i-1][j-1],  # Replace 
                                    dp[i-1][j],    # Delete
                                    dp[i][j-1]     # Insert
                                    )
    
    return dp[-1][-1]

def longestValidParentheses(s):
    stack, result = [(-1, ')')], 0
    for i, paren in enumerate(s):
        if paren == ')' and stack[-1][1] == '(':
            stack.pop()
            result = max(result, i - stack[-1][0])
        else:
            stack += (i, paren),
    return result