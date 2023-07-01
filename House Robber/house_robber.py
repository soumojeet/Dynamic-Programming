#House Robber Problem
#Greedy Approach

def house_robber(array, i=0):
    n=len(array)
    if i>=n:
        return 0
    else:
        return max(array[i]+house_robber(array,i+2),house_robber(array,i+1))

array = [4,8,12,1,2,10,3,6,8]
print("Greedy Approach:",house_robber(array))

#Top Down Approach

def house_robber_td(array, i=0, lookup=None):
    lookup = dict() if lookup == None else lookup
    if i in lookup:
        return lookup[i]
    n=len(array)
    if i>=n:
        return 0
    else:
        lookup[i] = max(array[i]+house_robber_td(array,i+2,lookup),house_robber_td(array,i+1,lookup))
        return lookup[i]

array = [4,8,12,1,2,10,3,6,8]
print("Top Down Approach:",house_robber_td(array))

#Bottom Up Approach

def house_robber_bu(array):
    n=len(array)
    if n==1:
        return array[0]
    before_prev_dp = array[0]
    prev_dp = max(array[0],array[1])
    for i in range(2,n):
        dp = max(array[i]+before_prev_dp,prev_dp)
        before_prev_dp=prev_dp
        prev_dp=dp
    return prev_dp

array = [4,8,12,1,2,10,3,6,8]
print("Bottom Up Approach:",house_robber_bu(array))