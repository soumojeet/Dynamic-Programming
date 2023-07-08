#Longest Increasing Subsequence Problem
#Greedy Approach

def longest_increasing_subsequence(array,i=0,prev=float("-inf")):
    n=len(array)
    if i==n:
        return 0
    elif array[i]<=prev:
        return longest_increasing_subsequence(array,i+1,prev)
    else:
        return max(1+longest_increasing_subsequence(array,i+1,array[i]), 
                   longest_increasing_subsequence(array,i+1,prev))

array=[7,5,2,4,7,2,3,6,4,5,12,1,7]
print("Greedy Approach:",longest_increasing_subsequence(array))

#Top Down Approach

def longest_increasing_subsequence_td(array,i=0,prev=float("-inf"),lookup=None):
    lookup=dict() if lookup is None else lookup
    if i in lookup:
        return lookup[i]
    n=len(array)
    if i==n:
        lookup[i]=0
        return lookup[i]
    elif array[i]<=prev:
        lookup[i]=longest_increasing_subsequence_td(array,i+1,prev)
        return lookup[i]
    else:
        lookup[i]=max(1+longest_increasing_subsequence_td(array,i+1,array[i]), 
                   longest_increasing_subsequence_td(array,i+1,prev))
        return lookup[i]

array=[7,5,2,4,7,2,3,6,4,5,12,1,7]
print("Top Down Approach:",longest_increasing_subsequence_td(array))

#Bottom Up Approach

def longest_increasing_subsequence_bu(array):
    n=len(array)
    dp=[0]*n
    dp[0]=1

    for i in range(1,n):
        maxlen=0
        for j in range(i):
            if array[j]<array[i] and dp[j]>maxlen:
                maxlen=dp[j]
        dp[i]=1+maxlen
    return max(dp)   

array=[7,5,2,4,7,2,3,6,4,5,12,1,7]
print("Bottom Up Approach:",longest_increasing_subsequence_bu(array))