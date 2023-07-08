#Equal Sum Partition Problem
#Greedy Approach

def equal_sum_partition(array,i=0,sum1=0,sum2=0):
    n=len(array)
    
    if i==n:
        return sum1==sum2
    else:
        return equal_sum_partition(array,i+1,sum1+array[i],sum2) or equal_sum_partition(array,i+1,sum1,sum2+array[i])

array = [4,5,3,2,5,1]
print("Greedy Approach:",equal_sum_partition(array))

#Bottom Up Approach

def equal_sum_partition_bu(array):
    array_sum = sum(array)
    array_sum_half = array_sum//2
    if array_sum%2 == 1:
        return False
    n=len(array)
    if n==0 or array_sum_half//2>sum(array):
        return False
    
    dp=[[0]*(array_sum_half+1) for i in range(n)]
    dp[0][0]=1
    if array[0]<=array_sum_half:
        dp[0][array[0]]=1
    for i in range(1,n):
        for j in range(array_sum_half+1):
            dp[i][j]=dp[i-1][j]+(dp[i-1][j-array[i]] if j-array[i] >= 0 else 0)
    return True if dp[n-1][array_sum_half]>0 else False

array = [4,5,3,2,5,1]
print("Bottom Up Approach:",equal_sum_partition_bu(array))