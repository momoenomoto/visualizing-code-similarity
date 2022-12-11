def longestPalindrome(s):
    lenS = len(s)
    if lenS <= 1: return s
    minStart, maxLen, i = 0, 1, 0
    while i < lenS:
        if lenS - i <= maxLen / 2: break
        j, k = i, i
        while k < lenS - 1 and s[k] == s[k + 1]: k += 1
        i = k + 1
        while k < lenS - 1 and j and s[k + 1] == s[j - 1]:  k, j = k + 1, j - 1
        if k - j + 1 > maxLen: minStart, maxLen = j, k - j + 1
    return s[minStart: minStart + maxLen]
    
def trap(height):
    ans = 0
    for i in range(1,len(height)-1): 
        max_left = max(height[:i])
        max_right = max(height[i+1:])
        potential = min(max_left, max_right) - height[i]
        ans += max(0, potential) 
    return ans

def minPathSum(grid):
    row =  len(grid)
    column = len(grid[0])
    
    # Craft graphs
    heap = []
    sum = defaultdict(list)
    cost = defaultdict(list)
    graph = defaultdict(list)
    seen = defaultdict(list)
    for r in range (0, row):
        for c in range (0, column):
            sum[r,c] = float('inf')
            cost[r,c].append(grid[r][c])
            # check right
            if c < column - 1:
                graph[r,c].append([r,c+1])
            # check down
            if r < row - 1:
                graph[r,c].append([r+1,c])
  
    # Setup for start and end
    min_node = (0,0)
    end_node = ((row-1),(column-1))   
    sum[(min_node)] = cost.get(min_node)[0]
    seen[(min_node)] = True
    
    while len(seen) > 0:
        # check attached nodes
        if graph.get(min_node):
            # Visit next mini-value node and relax it's edge
            for node in graph.get(min_node):
                n = tuple(node)
                visit_cost = cost.get(n)[0] + (sum.get(min_node))
                # Check if relaxing has reduced the cost
                if visit_cost < sum.get(n):
                    # Update the cost for each updated node
                    sum[(n)] = visit_cost
                    # Add to head future nodes to visit
                    heappush(heap, (visit_cost, n))
                    seen[(n)] = True

        seen.pop(min_node)

        # Check Next Cost Optimized with a heap
        if len(heap) > 0:
            next_min_node = heappop(heap)[1]
            min_node = next_min_node

    return sum.get(end_node)

def editDistance(word1, word2):
    if len(word1) == 0 or len(word2) == 0:
        return max(len(word1), len(word2))
    dist = range(len(word2) + 1)
    for i in xrange(len(word1)):
        dist_ij, dist[0] = i, i + 1
        for j in xrange(len(word2)):
            if word1[i] == word2[j]:
                dist_ij, dist[j + 1] = dist[j + 1], dist_ij
            else:
                dist_ij, dist[j + 1] = dist[j + 1], min(dist[j], dist[j + 1], dist_ij) + 1
    return dist[-1]

def longestValidParentheses(s):
    s = ")" + s  
    stack, ans = [], 0
    for index in xrange(len(s)):
      element = s[index]
      if element == ")" and stack and stack[-1][1] == "(":
        stack.pop()
        ans = max(ans, index - stack[-1][0])
      else:
        stack.append((index, element))
    return ans