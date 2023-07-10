#Minimum Cost Tickets Problem
#Greedy Approach

def minimum_cost_tickets(travel_days, costs, no_of_days, day=0):
    if day>=no_of_days:
        return 0
    elif day not in travel_days:
        return minimum_cost_tickets(travel_days, costs, no_of_days, day+1)
    else:
        return min(costs[0]+minimum_cost_tickets(travel_days, costs, no_of_days, day+1),
                   costs[1]+minimum_cost_tickets(travel_days, costs, no_of_days, day+7),
                   costs[2]+minimum_cost_tickets(travel_days, costs, no_of_days, day+30))

travel_days=[1,3,8,9,22,23,28,31]
costs=[4,10,25]
no_of_days=32
print("Greedy Approach:",minimum_cost_tickets(travel_days,costs,no_of_days))

#Top Down Approach

def minimum_cost_tickets_td(travel_days, costs, no_of_days, day=0, lookup=None):
    lookup = dict() if lookup is None else lookup
    if day in lookup:
        return lookup[day]
    if day>=no_of_days:
        lookup[day]=0
        return lookup[day]
    elif day not in travel_days:
        lookup[day]=minimum_cost_tickets_td(travel_days, costs, no_of_days, day+1, lookup)
        return lookup[day]
    else:
        lookup[day]=min(costs[0]+minimum_cost_tickets_td(travel_days, costs, no_of_days, day+1, lookup),
                   costs[1]+minimum_cost_tickets_td(travel_days, costs, no_of_days, day+7, lookup),
                   costs[2]+minimum_cost_tickets_td(travel_days, costs, no_of_days, day+30, lookup))
        return lookup[day]

travel_days=[1,3,8,9,22,23,28,31]
costs=[4,10,25]
no_of_days=32
print("Top Down Approach:",minimum_cost_tickets_td(travel_days,costs,no_of_days))

#Bottom Up Approach

def minimum_cost_tickets_bu(travel_days, costs, no_of_days):
    dp=[0]*no_of_days
    for i in range(len(dp)):
        if i not in travel_days:
            dp[i]=(dp[i-1] if i-1 >= 0 else 0)
        else:
            day_cost= costs[0]+(dp[i-1] if i-1 >= 0 else 0)
            week_cost= costs[1]+(dp[i-7] if i-7 >= 0 else 0)
            month_cost= costs[2]+(dp[i-30] if i-30 >= 0 else 0)
            dp[i] = min(day_cost, week_cost, month_cost)
    return dp[no_of_days-1]

travel_days=[1,3,8,9,22,23,28,31]
costs=[4,10,25]
no_of_days=32
print("Bottom Up Approach:",minimum_cost_tickets_bu(travel_days,costs,no_of_days))