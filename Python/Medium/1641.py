from itertools import accumulate

def countVowelStrings(n):
    dp = [1] * 5
    for i in range(n):
        dp = accumulate(dp)
    return list(dp)[-1]

# Since we have to return it in lexicographically sorted for all valid i, s[i]
# that means each letter will have less combinations so we add each combinations
# for every n and return the largest which will be at the last index
# 1,2,3,4,5 -> 1,3,6,10,15 -> 1,4,10,20,35
# a,e,i,o,u -> aa,ae,ai,ao,au,ee,ei,eo,eu,ii,io,iu,oo,ou,uu
n = 3
counted = countVowelStrings(n)
print(counted)
