def longestPalindrome(s):

    dp = [[False]*len(s) for _ in range(len(s)) ]
    for i in range(len(s)):
        dp[i][i]=True
    ans=s[0]
    for j in range(len(s)):
        for i in range(j):
            if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                dp[i][j]=True
                if j-i+1>len(ans):
                    ans=s[i:j+1]
    return ans
    
def trap(height):
    i, j, ans, mx, mi = 0, len(height) - 1, 0, 0, 0
    while i <= j:
        mi = min(height[i], height[j])
        mx = max(mx, mi)
        ans += mx - mi
        if height[i] < height[j]: i += 1
        else: j -= 1
    return ans

def minPathSum(grid):
    from heapq import heappush, heappop
    h = []
    startNode = (grid[0][0], (0,0)) # cost, coor
    heappush(h, startNode)
    dirs = [(1,0), (0,1)] # only right and down are allowed
    cost_so_far = {(0,0): grid[0][0]} # stores min cost to get to all nodes
    # cameFrom = {(0,0): None} # -- NOTE [1]
    while h:
        cost, node = heappop(h)
        x, y = node
        if x == len(grid)-1 and y == len(grid[0])-1: # destination found
            break   
        # explore nei
        for dir in dirs:
            newX, newY = x+dir[0], y+dir[1]
            # check bounds
            if newX <= len(grid)-1 and newY <= len(grid[0])-1:
                edgeCost, nei = grid[newX][newY], (newX, newY)
                newCost = cost + edgeCost 
                # check if weights needs to be updated
                if ( nei not in cost_so_far or (nei in cost_so_far and cost_so_far[nei] > newCost) ):
                    cost_so_far[nei] = newCost
                    heappush(h, (newCost, nei)) 
    # return cost to reach destination
    return cost_so_far[(x,y)]

def editDistance(s1, s2):
    @lru_cache(maxsize=None)
    def f(i, j):
        if i == 0 and j == 0: return 0
        if i == 0 or j == 0: return i or j
        if s1[i - 1] == s2[j - 1]:
            return f(i - 1, j - 1)
        return min(1 + f(i, j - 1), 1 + f(i - 1, j), 1 + f(i - 1, j - 1))

    m, n = len(s1), len(s2)
    return f(m, n)

def longestValidParentheses(s):
    max_length = 0
                
    l,r=0,0        
    for i in range(len(s)):
        if s[i] == '(':
            l+=1
        else:
            r+=1                        
        if l == r:# valid balanced parantheses substring 
            max_length=max(max_length, l*2)
        elif r>l: # invalid case as ')' is more
            l=r=0
    
    l,r=0,0        
    # traverse the string from right to left
    for i in range(len(s)-1,-1,-1):
        if s[i] == '(':
            l+=1
        else:
            r+=1            
        if l == r:# valid balanced parantheses substring 
            max_length=max(max_length, l*2)
        elif l>r: # invalid case as '(' is more
            l=r=0
    return max_length