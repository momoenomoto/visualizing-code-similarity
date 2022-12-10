def longestPalindrome(s):
	t = '^#'+'#'.join(s)+'#$'
	n = len(t)
	p = [0]*n
	c = r = cm = rm = 0
	for i in range (1, n-1):
		p[i] = min(r-i, p[2*c-i]) if r > i else 0
		while t[i-p[i]-1] == t[i+p[i]+1]: p[i] += 1
		if p[i]+i > r: c, r = i, p[i]+i
		if p[i] > rm: cm, rm = i, p[i]
	return s[(cm-rm)//2:(cm+rm)//2]
    
def trap(height):
    left = [0] * len(height)
    for i in range(1, len(height)):
        left[i] = max(left[i - 1], height[i - 1])
    
    right = [0] * len(height)
    for i in range(len(height) - 2, -1, -1):
        right[i] = max(right[i + 1], height[i + 1])

    total = 0
    for i, curr in enumerate(height):
        total += max(0, min(left[i], right[i]) - curr)        
    return total

def minPathSum(grid):
    nR = len(grid)
    nC = len(grid[0])
    adj = [(1, 0), (0, 1)]
    
    @cache
    def dfs(r, c):
        if r == nR - 1 and c == nC - 1:
            return grid[r][c]
        paths = []
        for a, b in adj:
            r2, c2 = r + a, c + b
            if 0 <= r2 < nR and 0 <= c2 < nC:
                paths.append(dfs(r2, c2))
        return grid[r][c] + min(paths)
    return dfs(0, 0)

def editDistance(word1, word2):
    def find_distance(word1, word1_pointer, word2, word2_pointer, memo):
        if word1_pointer == len(word1) and word2_pointer == len(word2):
            return 0
        
        if word1_pointer == len(word1) or word2_pointer == len(word2):
            return max(len(word1) - word1_pointer, len(word2) - word2_pointer)
        
        key = (word1_pointer, word2_pointer)
        if key in memo: return memo[key]
        
        if word1[word1_pointer] == word2[word2_pointer]:
            memo[key] = find_distance(word1, word1_pointer + 1, word2, word2_pointer + 1, memo)
        else:
            memo[key] =  1 + make_move(word1, word1_pointer, word2, word2_pointer, memo)
            
        return memo[key]
    
    
    def make_move(word1, word1_pointer, word2, word2_pointer, memo):
        return min(
                find_distance(word1, word1_pointer + 1, word2, word2_pointer + 1, memo), # update
                find_distance(word1, word1_pointer, word2, word2_pointer + 1, memo), # insert
                find_distance(word1, word1_pointer + 1, word2, word2_pointer, memo) # delete
            )
    return find_distance(word1, 0, word2, 0, {})

def longestValidParentheses(s):
    open_=0
    close=0
    ans1=0
    for i in s:
        if i=='(':
            open_+=1
        else:
            close+=1
        if open_==close:
            ans1=max(close*2,ans1)
        elif close>open_:
            open_=close=0
    ans2=0
    open_=close=0
    for i in range(len(s)-1,-1,-1):
        if s[i]=='(':
            open_+=1
        else:
            close+=1
        if open_==close:
            ans2=max(ans2,2*open_)
        elif open_>close:
            open_=close=0
    return max(ans1,ans2)