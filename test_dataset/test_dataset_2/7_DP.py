def longestPalindrome(s):
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range (1, n-1):
        P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

    
def trap(height):
    h_len = len(height)
    biggest_left: list[int] = [height[0]] * h_len
    biggest_right: list[int] = [height[-1]] * h_len

    for i in range(1, h_len):
        biggest_left[i] = max(biggest_left[i-1], height[i])
        biggest_right[-i-1] = max(biggest_right[-i], height[-i-1])
    
    return sum(min(biggest_left[i], biggest_right[i]) - height[i] for i in range(h_len))

def minPathSum(grid):
    minPathCost = float('inf')
    stack = [( (0,0), grid[0][0] )]
    trgtX, trgtY = len(grid)-1, len(grid[0])-1
    dirs = [(1,0), (0,1)]
    while stack:
        (x,y), pathCost = stack.pop()

        if (x,y) == (trgtX, trgtY): # only capture pathCost when path is fully traversed (aka rigt-bottm corner cell is reached)
            minPathCost = min(minPathCost, pathCost)

        for dir in dirs:
            newX, newY = x+dir[0], y+dir[1]
            if newX <= trgtX and newY <= trgtY:
                stack.append( ( (newX, newY), pathCost+grid[newX][newY] ) )

    return minPathCost

def editDistance(word1, word2):
    memo = {}
        
    def dfs(i, j):
        if i == 0 or j == 0: return j or i
                    
        if (i,j) in memo:
            return memo[(i,j)]
        
        if word1[i-1] == word2[j-1]:
            ans = dfs(i-1, j-1)
        else: 
            ans = 1 + min(dfs(i, j-1), dfs(i-1, j), dfs(i-1, j-1))
            
        memo[(i,j)] = ans
        return memo[(i,j)]
    
    return dfs(len(word1), len(word2))

def longestValidParentheses(S):
    stack, ans = [-1], 0
    for i in range(len(S)):
        if S[i] == '(': stack.append(i)
        elif len(stack) == 1: stack[0] = i
        else:
            stack.pop()
            ans = max(ans, i - stack[-1])
    return ans