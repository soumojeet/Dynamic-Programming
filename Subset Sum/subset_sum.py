#Subset Sum Problem
#Greedy Approach

def subset_sum(array,value,i=0):
    n=len(array)
    
    if value==0:
        return 1
    elif i==n or value<0:
        return 0
    else:
        return subset_sum(array,value-array[i],i+1)+subset_sum(array,value,i+1)

array=[1,2,3,1,4]
value=6
print("Greedy Approach:",subset_sum(array,value))

#Top Down Approach

def subset_sum_td(array,value,i=0,lookup=None):
    lookup = dict() if lookup is None else lookup
    if (i,value) in lookup:
        return lookup[(i,value)]
    n=len(array)
    
    if value==0:
        lookup[(i,value)]=1
        return lookup[(i,value)]
    elif i==n or value<0:
        lookup[(i,value)]=0
        return lookup[(i,value)]
    else:
        lookup[(i,value)]=subset_sum_td(array,value-array[i],i+1,lookup)+subset_sum_td(array,value,i+1,lookup)
        return lookup[(i,value)]

array=[1,2,3,1,4]
value=6
print("Top Down Approach:",subset_sum_td(array,value))

#Bottom Up Approach

def subset_sum_bu(array,value):
    n=len(array)
    if value>sum(array) or n==0:
        return 0
    prev_dp=[0]*(value+1)
    dp=[0]*(value+1)
    prev_dp[0]=1
    
    if array[0]<=value:
        prev_dp[array[0]]=1
    
    for i in range(1,n):
        for j in range(value+1):
            dp[j]=prev_dp[j]+(prev_dp[j-array[i]] if j-array[i]>=0 else 0)
        prev_dp=dp
        dp=[0]*(value+1)
    return prev_dp[value]

array=[1,2,3,1,4]
value=6
print("Bottom Up Approach:",subset_sum_bu(array,value))