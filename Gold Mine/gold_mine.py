#Gold Mine Problem
#Greedy Approach

def gold_mine(matrix, i=0, j=0):
    n=len(matrix)
    m=len(matrix[0])
    
    if i==n or j==m or j<0:
        return 0
    else:
        return matrix[i][j] + max(gold_mine(matrix, i+1, j-1),
                                  gold_mine(matrix, i+1, j),
                                  gold_mine(matrix, i+1, j+1))

matrix = [[3,2,12,15,10],[6,19,7,11,17],[8,5,12,32,21],[3,20,2,9,7]]
max_gold = 0
for i in range(len(matrix[0])):
    max_gold = max(max_gold, gold_mine(matrix, 0, i))
print("Greedy Approach:",max_gold)

#Top Down Approach

def gold_mine_td(matrix, i=0, j=0, lookup=None):
    if (i,j) in lookup:
        return lookup[(i,j)]

    n=len(matrix)
    m=len(matrix[0])
    
    if i==n or j==m or j<0:
        lookup[(i,j)] = 0
        return lookup[(i,j)]
    else:
        lookup[(i,j)] = matrix[i][j] + max(gold_mine_td(matrix, i+1, j-1, lookup),
                                          gold_mine_td(matrix, i+1, j, lookup),
                                          gold_mine_td(matrix, i+1, j+1, lookup))
        return lookup[(i,j)]

matrix = [[3,2,12,15,10],[6,19,7,11,17],[8,5,12,32,21],[3,20,2,9,7]]
max_gold = 0
lookup = dict()
for i in range(len(matrix[0])):
    max_gold = max(max_gold, gold_mine_td(matrix, 0, i, lookup))
print("Top Down Approach:",max_gold)

#Bottom Up Approach

def gold_mine_bu(matrix):
    n=len(matrix)
    m=len(matrix[0])
    dp=[0]*m
    prev_dp=[0]*m
    
    for i in range(m):
        prev_dp[i]=matrix[0][i]
    for i in range(1,n):
        for j in range(m):
            top_left=prev_dp[j-1] if j-1>=0 else 0
            top=prev_dp[j]
            top_right=prev_dp[j+1] if j+1<m else 0
            dp[j]=matrix[i][j]+max(top_left,top,top_right)
        prev_dp=dp
        dp=[0]*m
    return max(prev_dp)

matrix = [[3,2,12,15,10],[6,19,7,11,17],[8,5,12,32,21],[3,20,2,9,7]]
print("Bottom Up Approach:",gold_mine_bu(matrix))