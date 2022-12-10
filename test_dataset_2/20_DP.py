def longestPalindrome(s):
	L, M, x = len(s), 0, 0
	for i in range(L):
		for a,b in [(i,i),(i,i+1)]:
			while a >= 0 and b < L and s[a] == s[b]: a -= 1; b += 1
			if b - a - 1 > M: M, x = b - a - 1, a + 1
	return s[x:x+M]
    
def trap(height):
    walls = {}
    dec_mono_stack = []
    
    for i, v in enumerate(height):
        while dec_mono_stack and v > height[dec_mono_stack[-1]]:
            mid_index = dec_mono_stack.pop()
            if not dec_mono_stack:
                # no left wall, can't trap
                break
            left_wall_i = dec_mono_stack[-1]
            right_wall_i = i
            height_val = min(height[left_wall_i], height[right_wall_i]) - height[mid_index]
            walls[(left_wall_i, right_wall_i)] = height_val * (right_wall_i - left_wall_i - 1)
            
        dec_mono_stack.append(i)
            
    return sum(walls.values())

def minPathSum(grid):
    m,n = len(grid),len(grid[0])
    for row in range(m):
        for col in range(n):
            #first element must be kept as it is
            if row==0 and col ==0:
                continue
            #first row across addition
            elif row ==0 and col!=0:
                grid[row][col] = grid[row][col]+grid[row][col-1]
            #first column downwards addition
            elif row!=0 and col==0:
                grid[row][col] = grid[row][col]+grid[row-1][col]
            #for all the matrix elements except the row==0 and col ==0
            else:
                grid[row][col] = grid[row][col] + min(grid[row][col-1],grid[row-1][col])
    
    return grid[row][col]

def editDistance(word1, word2):
    d = [range(len(word2)+1)] + [[row]*(len(word2)+1) for row in range(1, len(word1)+1)]
    for i in range(1, len(d)):
        for j in range(1, len(d[0])):
            d[i][j] = d[i-1][j-1] if word1[i-1] == word2[j-1] else min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
    return d[-1][-1]

def longestValidParentheses(s):
    n = len(s)
    dp = [0] * n
    ans = 0
    
    for i in range(1,n):
        if s[i] == ')' and s[i - 1] == '(':
            dp[i] = dp[i-2] + 2;
        elif s[i] == ')' and s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2;
        ans = max(ans, dp[i])
    
    return ans