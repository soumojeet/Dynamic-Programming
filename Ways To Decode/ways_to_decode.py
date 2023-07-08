#Ways To Decode Problem
#Greedy Approach

def ways_to_decode(string,i=0):
    n=len(string)
    
    if i==n:
        return 1
    elif string[i]=="0":
        return 0
    elif i+1<n and "10"<=string[i]+string[i+1]<="26":
        return ways_to_decode(string,i+1)+ways_to_decode(string,i+2)
    else:
        return ways_to_decode(string,i+1)

string="512810120129"
print("Greedy Approach:",ways_to_decode(string))

#Top Down Approach

def ways_to_decode_td(string,i=0,lookup=None):
    lookup=dict() if lookup is None else lookup
    if i in lookup:
        return lookup[i]
    n=len(string)
    
    if i==n:
        lookup[i]=1
        return lookup[i]
    elif string[i]=="0":
        lookup[i]=0
        return lookup[i]
    elif i+1<n and "10"<=string[i]+string[i+1]<="26":
        lookup[i]=ways_to_decode_td(string,i+1,lookup)+ways_to_decode_td(string,i+2,lookup)
        return lookup[i]
    else:
        lookup[i]=ways_to_decode_td(string,i+1,lookup)
        return lookup[i]

string="512810120129"
print("Top Down Approach:",ways_to_decode_td(string))

#Bottom Up Approach

def ways_to_decode_bu(string):
    n=len(string)
    if string[0]=="0":
        return 0
    elif n==1:
        return 1
    before_prev_dp=1
    prev_dp=int(string[1]!="0")+int("10"<=string[0]+string[1]<="26")
    
    for i in range(2,n):
        dp=0
        if string[i]!="0":
            dp+=prev_dp
        if "10"<=string[i-1]+string[i]<="26":
            dp+=before_prev_dp
        before_prev_dp=prev_dp
        prev_dp=dp
    return prev_dp

string="512810120129"
print("Bottom Up Approach:",ways_to_decode_bu(string))