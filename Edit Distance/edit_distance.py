#Edit Distance Problem
#Greedy Approach

def edit_distance(word1, word2, i=0, j=0):
    n=len(word1)
    m=len(word2)
    
    if i==n:
        return n-j
    elif j==m:
        return m-i
    elif word1[i]==word2[j]:
        return edit_distance(word1, word2, i+1, j+1)
    else:
        return 1 + min(edit_distance(word1, word2, i+1, j), 
                       edit_distance(word1, word2, i, j+1), 
                       edit_distance(word1, word2, i+1, j+1))

word1="index"
word2="inside"
print("Greedy Approach:",edit_distance(word1,word2))

#Top Down Approach

def edit_distance_td(word1, word2, i=0, j=0, lookup=None):
    lookup = dict() if lookup == None else lookup
    if (i,j) in lookup:
        return lookup[(i,j)]
    
    n=len(word1)
    m=len(word2)
    
    if i==n:
        return n-j
    elif j==m:
        return m-i
    elif word1[i]==word2[j]:
        lookup[(i,j)]=edit_distance(word1, word2, i+1, j+1)
        return lookup[(i,j)]
    else:
        lookup[(i,j)]=1+min(edit_distance_td(word1, word2, i+1, j, lookup), 
                              edit_distance_td(word1, word2, i, j+1, lookup), 
                              edit_distance_td(word1, word2, i+1, j+1, lookup))
        return lookup[(i,j)]

word1="index"
word2="inside"
print("Top Down Approach:",edit_distance_td(word1,word2))

#Bottom Up Approach

def edit_distance_bu(word1,word2):
    n=len(word1)
    m=len(word2)
    dp=[0]*(n+1)
    prev_dp=[0]*(n+1)
    
    dp[0]=0
    for i in range(0,n+1):
        prev_dp[i]=i
    for i in range(1,m+1):
        dp[0]=i
        for j in range(1,n+1):
            if word1[j-1]==word2[i-1]:
                dp[j]=prev_dp[j-1]
            else:
                dp[j]=1+min(prev_dp[j], prev_dp[j-1], dp[j-1])
        prev_dp=dp
        dp=[0]*(n+1)
    return prev_dp[n]

word1="inside"
word2="index"
print("Bottom Up Approach:",edit_distance_bu(word1,word2))