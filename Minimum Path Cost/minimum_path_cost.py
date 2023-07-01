#Minimum Path Cost Problem
#Greedy Approach

def minimum_path_cost(matrix, i=0, j=0):
    n=len(matrix)
    m=len(matrix[0])
    
    if i==n-1 and j==m-1:
        return matrix[i][j]
    elif i==n-1:
        return matrix[i][j] + minimum_path_cost(matrix,i,j+1)
    elif j==m-1:
        return matrix[i][j] + minimum_path_cost(matrix,i+1,j)
    else:
        return matrix[i][j] + min(minimum_path_cost(matrix,i+1,j), minimum_path_cost(matrix,i,j+1))

matrix = [[3,2,12,15,10],[6,19,7,11,17],[8,5,12,32,21],[3,20,2,9,7]]
print("Greedy Approach:",minimum_path_cost(matrix))

#Top Down Approach

def minimum_path_cost_td(matrix, i=0, j=0, lookup=None):
    lookup = dict() if lookup == None else lookup
    if (i,j) in lookup:
        return lookup[(i,j)]

    n=len(matrix)
    m=len(matrix[0])
    
    if i==n-1 and j==m-1:
        lookup[(i,j)] = matrix[i][j]
        return lookup[(i,j)]
    elif i==n-1:
        lookup[(i,j)] = matrix[i][j] + minimum_path_cost_td(matrix,i,j+1,lookup)
        return lookup[(i,j)]
    elif j==m-1:
        lookup[(i,j)] = matrix[i][j] + minimum_path_cost_td(matrix,i+1,j,lookup)
        return lookup[(i,j)]
    else:
        lookup[(i,j)] = matrix[i][j] + min(minimum_path_cost_td(matrix,i+1,j,lookup), minimum_path_cost_td(matrix,i,j+1,lookup))
        return lookup[(i,j)]

matrix = [[3,2,12,15,10],[6,19,7,11,17],[8,5,12,32,21],[3,20,2,9,7]]
print("Top Down Approach:",minimum_path_cost_td(matrix))

#Bottom Up Approach

def minimum_path_cost_bu(matrix):
    n=len(matrix)
    m=len(matrix[0])
    dp=[0]*m
    prev_dp=[0]*m
    prev_dp[0] = matrix[0][0]
    
    for i in range(1,m):
        prev_dp[i]=prev_dp[i-1]+matrix[0][i]
    for i in range(1,n):
        dp[0]=prev_dp[0]+matrix[i][0]
        for j in range(1,m):
            dp[j]=matrix[i][j] + min(dp[j-1], prev_dp[j])
        prev_dp=dp
        dp=[0]*m
    return prev_dp[m-1]    

matrix = [[3,2,12,15,10],[6,19,7,11,17],[8,5,12,32,21],[3,20,2,9,7]]
print("Bottom Up Approach:",minimum_path_cost_bu(matrix))