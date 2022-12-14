def whole():
    def longestPalindrome(s):
        t = '^#'+'#'.join(s)+'#$'
        c = r = 0                             # center and radius
        for i in range(1,len(t)-1):
            j = 1 if t[i] == '#' else 2       # skip '#' and check letters only
            while  t[i-j] == t[i+j]: j += 2
            if j > r: c, r = i, j
        return s[(c-r+1)//2:(c+r-1)//2]
        
    def trap(height):
        total = 0
        for i, curr in enumerate(height):
            left = 0 if i == 0 else max(height[:i])
            right = 0 if i == len(height) - 1 else max(height[i+1:])
            total += max(0, min(left, right) - curr)
        return total

    def minPathSum(grid):
        n=len(grid[0])
        prev=[-1]*n
        for i in range(m):
            curr=[-1]*n
            for j in range(n):
                if i==0 and j==0:
                    curr[0]=grid[0][0]
                else:
                    up=grid[i][j]
                    if i>0:
                        up+=prev[j]
                    else:
                        up+=10000000000000
                        
                    left=grid[i][j]
                    if j>0:
                        left+=curr[j-1]
                    else:
                        left+=10000000000000
                        
                    curr[j]=min(up,left)
            prev=curr
                    
        return prev[n-1]

    def editDistance(word1, word2):
        m=len(word1)
        n=len(word2)
        prev=[0]*(n+1)
        for j in range(n+1):
            prev[j]=j
        for i in range(1,m+1):
            curr=[0]*(n+1)
            curr[0]=i
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    curr[j]=prev[j-1]
                else:
                    curr[j]= 1 + min(prev[j],min(curr[j-1],prev[j-1]))
            prev=curr
        return curr[-1]

    def longestValidParentheses(s):
        m = l = r = 0
        for e in s:
            if e=='(':
                l+=1
            else:
                r+=1
            if l==r:
                m = max(m,r+l)
            elif r>l:
                l=r=0
        l=r=0
        for e in s[::-1]:
            if e==')':
                r+=1
            else: 
                l+=1
            if l==r: 
                m=max(m,r+l)
            elif l>r:
                l=r=0
        return m