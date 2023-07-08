#Shortest Common Subsequence Problem
#Greedy Approach

def shortest_common_subsequence(string1,string2,i=0,j=0):
    len1=len(string1)
    len2=len(string2)
    
    if i==len1:
        return len2-j
    elif j==len2:
        return len1-i
    elif string1[i]==string2[j]:
        return 1+shortest_common_subsequence(string1,string2,i+1,j+1)
    else:
        return 1+min(shortest_common_subsequence(string1,string2,i+1,j), 
                     shortest_common_subsequence(string1,string2,i,j+1))

string1="abdacbab"
string2="acebfca"
print("Greedy Approach:",shortest_common_subsequence(string1,string2))

#Top Down Approach

def shortest_common_subsequence_td(string1,string2,i=0,j=0,lookup=None):
    lookup = dict() if lookup == None else lookup
    if (i,j) in lookup:
        return lookup[(i,j)]

    len1=len(string1)
    len2=len(string2)
    
    if i==len1:
        lookup[(i,j)]=len2-j
        return lookup[(i,j)]
    elif j==len2:
        lookup[(i,j)]=len1-i
        return lookup[(i,j)]
    elif string1[i]==string2[j]:
        lookup[(i,j)]=1+shortest_common_subsequence_td(string1,string2,i+1,j+1)
        return lookup[(i,j)]
    else:
        lookup[(i,j)]=1+min(shortest_common_subsequence_td(string1,string2,i+1,j), 
                            shortest_common_subsequence_td(string1,string2,i,j+1))
        return lookup[(i,j)]

string1="abdacbab"
string2="acebfca"
print("Top Down Approach:",shortest_common_subsequence_td(string1,string2))

#Bottom Up Approach

def shortest_common_subsequence_bu(string1,string2):
    len1=len(string1)
    len2=len(string2)
    dp=[[0]*(len2+1) for i in range(len1+1)]
    for i in range(1,len1+1):
        dp[i][0]=i
    for i in range(1,len2+1):
        dp[0][i]=i
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if string1[i-1]==string2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1])
    return dp[len1][len2]

string1="abdacbab"
string2="acebfca"

print("Bottom Up Approach:",shortest_common_subsequence_bu(string1,string2))