#Coin Change Problem
#Greedy Approach

def coin_change(amount,possible_coins):
    if amount==0:
        return 0
    else:
        min_coins=float('inf')
        for coin in possible_coins:
            if amount-coin>=0:
                min_coins=min(min_coins,1+coin_change(amount-coin,possible_coins))
        return min_coins

amount=15
possible_coins=[2,3,7]
print("Greedy Approach:",coin_change(amount,possible_coins))

#Top Down Approach

def coin_change_td(amount,possible_coins,lookup=None):
    lookup = dict() if lookup == None else lookup
    if amount in lookup:
        return lookup[amount]
    if amount==0:
        lookup[amount]=0
        return lookup[amount]
    else:
        min_coins=float('inf')
        for coin in possible_coins:
            if amount-coin>=0:
                min_coins=min(min_coins,1+coin_change(amount-coin,possible_coins))
        lookup[amount]=min_coins
        return lookup[amount]

amount=15
possible_coins=[2,3,7]
print("Top Down Approach:",coin_change_td(amount,possible_coins))

#Bottom Up Approach

def coin_change_bu(amount,possible_coins):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for value in range(1,amount+1):
        for coin in possible_coins:
            if value-coin>=0:
                dp[value]=min(dp[value],1+dp[value-coin])
    return dp[amount]

amount=15
possible_coins=[2,3,7]
print("Bottom Up Approach:",coin_change_bu(amount,possible_coins))