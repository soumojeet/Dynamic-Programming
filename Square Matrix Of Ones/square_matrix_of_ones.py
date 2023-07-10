#Square Matrix Of Ones Problem
#Greedy Approach

def matrix_of_ones(matrix, i=0, j=0):
    if i<0 or j<0 or matrix[i][j]==0:
        return 0
    else:
        return 1+min(matrix_of_ones(matrix, i-1, j),
                     matrix_of_ones(matrix, i, j-1),
                     matrix_of_ones(matrix, i-1, j-1))
def square_matrix_of_ones(matrix):
    n=len(matrix)
    m=len(matrix[0])
    max_size=0
    
    for i in range(n):
        for j in range(m):
            max_size=max(max_size,matrix_of_ones(matrix, i, j))
    return max_size**2

matrix = [[0,0,1,1,1,0],[1,0,1,1,1,1],[0,1,1,1,1,0],[1,1,1,1,0,1],[0,1,0,1,1,1]]
print("Greedy Approach:",square_matrix_of_ones(matrix))

#Top Down Approach

def matrix_of_ones_td(matrix, i=0, j=0, lookup=None):
    if (i,j) in lookup:
        return lookup[(i,j)]
    if i<0 or j<0 or matrix[i][j]==0:
        lookup[(i,j)]=0
        return lookup[(i,j)]
    else:
        lookup[(i,j)]=1+min(matrix_of_ones_td(matrix, i-1, j, lookup),
                            matrix_of_ones_td(matrix, i, j-1, lookup),
                            matrix_of_ones_td(matrix, i-1, j-1, lookup))
        return lookup[(i,j)]
def square_matrix_of_ones_td(matrix):
    n=len(matrix)
    m=len(matrix[0])
    max_size=0
    lookup=dict()
    for i in range(n):
        for j in range(m):
            max_size=max(max_size,matrix_of_ones_td(matrix, i, j, lookup))
    return max_size**2

matrix = [[0,0,1,1,1,0],[1,0,1,1,1,1],[0,1,1,1,1,0],[1,1,1,1,0,1],[0,1,0,1,1,1]]
print("Top Down Approach:",square_matrix_of_ones_td(matrix))

#Bottom Up Approach

def square_matrix_of_ones_bu(matrix):
    n=len(matrix)
    m=len(matrix[0])
    dp=[0]*m
    prev_dp=[0]*m
    prev_dp[0]=matrix[0][0]
    max_size=matrix[0][0]
    
    for i in range(1,m):
        prev_dp[i]=matrix[0][i]
        max_size=max(max_size, prev_dp[i])
        
    for i in range(1,n):
        dp[0]=matrix[i][0]
        for j in range(1,m):
            dp[j]= 0 if matrix[i][j]==0 else 1+min(prev_dp[j], dp[j-1], prev_dp[j-1])
        max_size=max(max_size, max(dp))
        prev_dp=dp
        dp=[0]*m
    return max_size**2    

matrix = [[0,0,1,1,1,0],[1,0,1,1,1,1],[0,1,1,1,1,0],[1,1,1,1,0,1],[0,1,0,1,1,1]]
print("Bottom Up Approach:",square_matrix_of_ones_bu(matrix))