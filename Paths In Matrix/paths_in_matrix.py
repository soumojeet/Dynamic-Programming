#Paths In Matrix Problem
#Greedy Approach

def paths_in_matrix(matrix,i=0,j=0):
    n=len(matrix)
    m=len(matrix[0])
    
    if i==n or j==m or matrix[i][j]==1:
        return 0
    elif i==n-1 and j==m-1:
        return 1
    else:
        return paths_in_matrix(matrix,i+1,j) + paths_in_matrix(matrix,i,j+1)

matrix = [[0,0,1,0,1],[0,0,0,0,1],[0,0,1,0,0],[1,0,0,0,0]]
print("Greedy Approach:",paths_in_matrix(matrix))

#Top Down Approach

def paths_in_matrix_td(matrix,i=0,j=0,lookup=None):
    lookup = dict() if lookup == None else lookup
    if (i,j) in lookup:
        return lookup[(i,j)]
    
    n=len(matrix)
    m=len(matrix[0])
    
    if i==n or j==m or matrix[i][j]==1:
        lookup[(i,j)]=0
        return lookup[(i,j)]
    elif i==n-1 and j==m-1:
        lookup[(i,j)]=1
        return lookup[(i,j)]
    else:
        lookup[(i,j)]=paths_in_matrix(matrix,i+1,j) + paths_in_matrix(matrix,i,j+1)
        return lookup[(i,j)]

matrix = [[0,0,1,0,1],[0,0,0,0,1],[0,0,1,0,0],[1,0,0,0,0]]
print("Top Down Approach:",paths_in_matrix_td(matrix))

#Bottom Up Approach

def paths_in_matrix_bu(matrix):
    n=len(matrix)
    m=len(matrix[0])
    dp=[0]*m
    prev_dp=[0]*m
    prev_dp[0]=1 if matrix[0][0]==0 else 0 
    
    for i in range(1,m):
        prev_dp[i]=prev_dp[i-1] if matrix[0][i]==0 else 0
    for i in range(1,n):
        dp[0]=prev_dp[0] if matrix[i][0]==0 else 0  
        for j in range(1,m):
            dp[j]=prev_dp[j]+dp[j-1] if matrix[i][j]==0 else 0
        prev_dp=dp
        dp=[0]*m
    return prev_dp[m-1]    

matrix = [[0,0,1,0,1],[0,0,0,0,1],[0,0,1,0,0],[1,0,0,0,0]]
print("Bottom Up Approach:",paths_in_matrix_bu(matrix))