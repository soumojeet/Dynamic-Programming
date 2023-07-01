#0-1 Knapsack Problem
#Greedy Approach

def _knapsack(values,weights,knapsack,i=0):
    len_value=len(values)
    len_weight=len(weights)
    
    if i==len_value:
        return 0
    elif weights[i]>knapsack:
        return _knapsack(values,weights,knapsack,i+1)
    else:
        return max(values[i]+_knapsack(values,weights,knapsack-weights[i],i+1),
                   _knapsack(values,weights,knapsack,i+1))

values=[20,30,15,25,10]
weights=[6,13,5,10,3]
knapsack=20
print("Greedy Approach:",_knapsack(values,weights,knapsack))

#Top Down Approach

def _knapsack_td(values,weights,knapsack,i=0,lookup=None):
    lookup = dict() if lookup == None else lookup
    if (knapsack,i) in lookup:
        return lookup[(knapsack,i)]
    len_value=len(values)
    len_weight=len(weights)
    
    if i==len_value:
        lookup[(knapsack,i)]=0
        return lookup[(knapsack,i)]
    elif weights[i]>knapsack:
        lookup[(knapsack,i)]=_knapsack_td(values,weights,knapsack,i+1,lookup)
        return lookup[(knapsack,i)]
    else:
        lookup[(knapsack,i)]=max(values[i]+_knapsack_td(values,weights,knapsack-weights[i],i+1,lookup),
                                 _knapsack_td(values,weights,knapsack,i+1,lookup))
        return lookup[(knapsack,i)]

values=[20,30,15,25,10]
weights=[6,13,5,10,3]
knapsack=20
print("Top Down Approach:",_knapsack_td(values,weights,knapsack))

#Bottom Up Approach

def _knapsack_bu(values,weights,knapsack):
    if knapsack==0:
        return 0
    elif knapsack>=sum(weights):
        return sum(values)
    len_value=len(values)
    len_weight=len(weights)
    prev_dp=[0]*(knapsack+1)
    dp=[0]*(knapsack+1)
    
    for i in range(weights[0],knapsack+1):
        prev_dp[i]=values[0]
    for i in range(1,len_value):
        for j in range(knapsack+1):
            if weights[i]>j:
                dp[j]=prev_dp[j]
            else:
                dp[j]=max(values[i]+prev_dp[j-weights[i]],prev_dp[j])
        prev_dp=dp
        dp=[0]*(knapsack+1)
    return prev_dp[knapsack]

values=[20,30,15,25,10]
weights=[6,13,5,10,3]
knapsack=20
print("Bottom Up Approach:",_knapsack_bu(values,weights,knapsack))