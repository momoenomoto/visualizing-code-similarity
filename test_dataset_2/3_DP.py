def longestPalindrome(s):

    longest_palindrom = ''
    dp = [[0]*len(s) for _ in range(len(s))]
    #filling out the diagonal by 1
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrom = s[i]
		
    # filling the dp table
    for i in range(len(s)-1,-1,-1):
        for j in range(i+1,len(s)):  
            if s[i] == s[j]:  #if the chars mathces
                if j-i ==1 or dp[i+1][j-1] is True:
                    dp[i][j] = True
                    if len(longest_palindrom) < len(s[i:j+1]):
                        longest_palindrom = s[i:j+1]
            
    return longest_palindrom
    
def trap(height):
    if len(height)<= 2:
        return 0
    ans = 0
    i = 1
    j = len(height) - 1
    
    lmax = height[0]
    rmax = height[-1]
    
    while i <=j:
        if height[i] > lmax:
            lmax = height[i]
        if height[j] > rmax:
            rmax = height[j]
        
        if lmax <= rmax:
            ans += lmax - height[i]
            i += 1
			
        else:
            ans += rmax - height[j]
            j -= 1 
    return ans

def minPathSum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i > 0 and j > 0:
                grid[i][j] = min(grid[i][j] + grid[i-1][j], grid[i][j] + grid[i][j-1])
            elif i > 0:
                grid[i][j] += grid[i-1][j]
            elif j > 0:
                grid[i][j] += grid[i][j-1]
        
    return grid[-1][-1]

def editDistance(word1, word2):
    h, w = len(word1)+1, len(word2)+1
    pre = [i for i in range(w)]
    for i in range(1, h):
        cur = [i for _ in range(w)]
        for j in range(1, w):
            cur[j] = min(pre[j-1]+(word1[i-1] != word2[j-1]), pre[j]+1, cur[j-1]+1)
        pre = cur
    return pre[-1]

def longestValidParentheses(s):
    max_length = 0
    stck=[-1] # initialize with a start index
    for i in range(len(s)):
        if s[i] == '(':
            stck.append(i)
        else:
            stck.pop()
            if not stck: # if popped -1, add a new start index
                stck.append(i)
            else:
                max_length=max(max_length, i-stck[-1]) # update the length of the valid substring
    return max_length