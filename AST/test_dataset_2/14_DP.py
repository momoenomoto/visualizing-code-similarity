def whole():
    def longestPalindrome(s):
        lengthS = len(s)
        if lengthS <= 1: return s
        StartMin, lengthMax, i = 0, 1, 0
        while i < lengthS:
            if lengthS - i <= lengthMax / 2: break
            j, k = i, i
            while k < lengthS - 1 and s[k] == s[k + 1]: k += 1
            i = k + 1
            while k < lengthS - 1 and j and s[k + 1] == s[j - 1]:  k, j = k + 1, j - 1
            if k - j + 1 > lengthMax: StartMin, lengthMax = j, k - j + 1
        return s[StartMin: StartMin + lengthMax]
        
    def trap(height):
        result = 0
        for i in range(1,len(height)-1): 
            maxL = max(height[:i])
            maxR = max(height[i+1:])
            candidate = min(maxL, maxR) - height[i]
            result += max(0, candidate) 
        return result

    def minPathSum(grid):
        dp=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                dp[row][col]=grid[row][col]
                if row==0 and col==0:
                    continue
                candidates=set()
                if col>0:
                    candidates.add(dp[row][col-1])
                if row>0:
                    candidates.add(dp[row-1][col])
                dp[row][col]+=min(candidates)
        return dp[-1][-1]

    def editDistance(word1, word2):
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        distance = range(len(word2) + 1)
        for i in range(len(word1)):
            distance_ij, distance[0] = i, i + 1
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    distance_ij, distance[j + 1] = distance[j + 1], distance_ij
                else:
                    distance_ij, distance[j + 1] = distance[j + 1], min(distance[j], distance[j + 1], distance_ij) + 1
        return distance[-1]

    def longestValidParentheses(s):
        stack, curr_longest, max_longest = [], 0, 0
        for c in s:
            if c == '(':
                stack.append(curr_longest)
                curr_longest = 0
            elif c == ')':
                if stack:
                    curr_longest += stack.pop() + 2
                    max_longest = max(max_longest, curr_longest)
                else:
                    curr_longest = 0
        return max_longest