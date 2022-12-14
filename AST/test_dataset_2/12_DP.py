def whole():
    def longestPalindrome(s):
        for i in range(len(s)):
            #what we need is only the left bottom part
            start = i
            end = i
            while start >= 0:
                #case1. if sub-string is 'a'
                if start == end:
                    dp[start][end] = True
                #case2. if sub-string is 'ab'
                #We need this case because start + 1 may larger than end - 1 if using case3 directly
                elif start + 1 == end:
                    dp[start][end] = s[start] == s[end]
                #case3. if sub-string is 'aba' 'abac' ..etc, i.e. len(sub) >= 3
                else:
                    dp[start][end] = dp[start+1][end-1] and (s[start] == s[end])

                #if dp[start][end] is palidromic, check is it longer than current solution
                if dp[start][end] and (end - start + 1) > (lcsEndIndex - lcsStartIndex + 1):
                    lcsStartIndex = start
                    lcsEndIndex = end

                start = start - 1

        return s[lcsStartIndex:lcsEndIndex+1]
        
    def trap(height):
        left=0
        maxleft=height[:]
        for i in range(len(height)):
            maxleft[i]=left
            if height[i]>left:
                left=height[i]
        right=0
        maxright=height[:]
        for i in range(len(height)-1,-1,-1):
            maxright[i]=right
            if height[i]>right:
                right=height[i]
        res=0
        for ind in range(len(height)):
            if min(maxleft[ind],maxright[ind])>height[ind]:
                res+=min(maxleft[ind],maxright[ind])-height[ind]
        return res

    def minPathSum(grid):
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
        
        q = deque()
        visited = set()
        q.append((0,0))
        
        while(q):
            row, col = q.popleft()
            if (row, col) in visited:
                continue
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                q.append((row, col+1))
                q.append((row+1, col))
                visited.add((row,col))
                if row == 0 and col == 0:
                    continue
                elif row == 0 and col > 0:
                    grid[row][col] += grid[row][col-1]
                elif col == 0:
                    grid[row][col] += grid[row-1][col]
                else:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        
            
        return grid[-1][-1]

    def editDistance(word1, word2):
        m, n = len(word1), len(word2)
        heap = [(0, 0, 0)]
        seen = set()
        
        while heap:
            distance, i, j = heappop(heap)
            if word1[i:] == word2[j:]:
                return distance

            if ((i, j) not in seen):
                seen.add((i, j))
                if (i < m and j < n and word1[i] == word2[j]):
                    heappush(heap, (distance, i+1, j+1))
                else:
                    for di, dj in (1,0), (0,1), (1,1):
                        next_i, next_j = i+di, j+dj
                        if (next_i <= m and next_j <= n):
                            heappush(heap, (distance+1, next_i, next_j))

    def longestValidParentheses(s):
        stack = [0,] # Initial value to handle "()"
        max_parenthesis = 0
        for bracket in s:
            if bracket == '(':
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2  # Add 2 when a ")" matches "("
                    max_parenthesis = max(max_parenthesis, stack[-1]) # Keep track of longest valid sequence
                else:
                    stack = [0]

        return max_parenthesis