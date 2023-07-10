#Rod Cutting Problem
#Greedy Approach

def rod_cutting(prices, cuts):
    max_price = 0
    for length in range(1, cuts+1):
        max_price = max(max_price, prices[length]+rod_cutting(prices, cuts-length))
    return max_price

prices=[0,1,3,5,6,7,9,10,11]
cuts=8
print("Greedy Approach:",rod_cutting(prices,cuts))

#Top Down Approach

def rod_cutting_td(prices, cuts, lookup=None):
    lookup = dict() if lookup == None else lookup
    if cuts in lookup:
        return lookup[cuts]

    max_price = 0
    for length in range(1, cuts+1):
        max_price = max(max_price, prices[length]+rod_cutting_td(prices, cuts-length, lookup))
    lookup[cuts] = max_price
    return max_price

prices=[0,1,3,5,6,7,9,10,11]
cuts=8
print("Top Down Approach:",rod_cutting_td(prices,cuts))

#Bottom Up Approach

def rod_cutting_bu(prices, cuts):
    dp = [0]*(cuts+1)
    for i in range(1, cuts+1):
        for length in range(1, i+1):
            dp[i] = max(dp[i], prices[length]+dp[i-length])
    return dp[cuts]

prices=[0,1,3,5,6,7,9,10,11]
cuts=8
print("Bottom Up Approach:",rod_cutting_bu(prices,cuts))