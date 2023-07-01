#Ways To Climb Problem
#Greedy Approach

def ways_to_climb(stairs,jumps):
    if stairs==0:
        return 1
    else:
        no_of_ways=0
        for jump in jumps:
            if stairs-jump>=0:
                no_of_ways+=ways_to_climb(stairs-jump,jumps)
        return no_of_ways
    
stairs=10
jumps=[2,4,5,8]
print("Greedy Approach:",ways_to_climb(stairs,jumps))

#Top Down Approach

def ways_to_climb_td(stairs,jumps,lookup=None):
    lookup=dict() if lookup is None else lookup
    if stairs in lookup:
        return lookup[stairs]
    if stairs==0:
        lookup[stairs]=1
        return lookup[stairs]
    else:
        no_of_ways=0
        for jump in jumps:
            if stairs-jump>=0:
                no_of_ways+=ways_to_climb_td(stairs-jump,jumps)
        lookup[stairs]=no_of_ways
        return lookup[stairs]

stairs=10
jumps=[2,4,5,8]
print("Top Down Approach:",ways_to_climb_td(stairs,jumps))

#Bottom Up Approach

def ways_to_climb_bu(stairs,jumps):
    dp=[0]*(stairs+1)
    dp[0]=1
    for stair in range(1,stairs+1):
        for jump in jumps:
            if stair-jump>=0:
                dp[stair]+=dp[stair-jump]
    return dp[stairs]

stairs=10
jumps=[2,4,5,8]
print("Bottom Up Approach:",ways_to_climb_bu(stairs,jumps))