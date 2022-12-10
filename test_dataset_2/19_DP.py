def longestPalindrome(s):
	t = '^#'+'#'.join(s)+'#$'
	c = r = 0                             
	for i in range(1,len(t)-1):
		j = 1 if t[i] == '#' else 2       
		while  t[i-j] == t[i+j]: j += 2
		if j > r: c, r = i, j
	return s[(c-r+1)//2:(c+r-1)//2]
    
def trap(height):
    tot = 0
    for i, cur in enumerate(height):
        if i == len(height) - 1:
            r = 0
        else: 
            l = max(height[i+1:])
            
        if i == 0:
            l = 0
        else:
            l = max(height[:i])
        
        tot += max(0, min(l, r) - cur)
    return tot

def minPathSum(grid):
    m=len(grid)
    n=len(grid[0])
    dp = []
    for j in range(m):
        for i in range(n):
                dp[j][i]=-1

    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                dp[0][0]=grid[0][0]
            else:
                up=grid[i][j]
                if i>0:
                    up+=dp[i-1][j]
                else:
                    up+=10000000000000
                    
                l=grid[i][j]
                if j>0:
                    l+=dp[i][j-1]
                else:
                    l+=10000000000000
                    
                dp[i][j]=min(up,l)
                
    return dp[m-1][n-1]

def editDistance(word1, word2):
    m, n =len(word1), len(word2)

    grid=[[0 for _ in range(n+1)]for j in range(m+1)]
    
    for i in range(m+1):
        grid[i][0]=i

    for j in range(n+1):
        grid[0][j]=j
        
    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1]==word2[j-1]:
                grid[i][j]= 0 + grid[i-1][j-1]
            else:
                grid[i][j]= 1 + min(grid[i-1][j],grid[i][j-1],grid[i-1][j-1])
    return grid[m][n]

def longestValidParentheses(string):
    mid = l = r = 0

    for ele in string:
        if ele == '(':
            l+=1
        else:
            r+=1
        if l == r:
            mid = max(mid,r+l)
        elif r > l:
            l = r = 0
        
    l = r = 0
    for ele in string[::-1]:
        if ele == ')':
            r += 1
        else: 
            l +=1
        if l ==r: 
            mid=max(mid, r +l)
        elif l>r:
            l=r=0
    return mid