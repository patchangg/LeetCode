from collections import Counter

def findLHS(nums):
    counted = Counter(nums)
    output = 0

    for n in counted:
        if n+1 in counted:
            output = max(output, counted[n] + counted[n+1])

    return output

nums = [1,3,2,2,5,2,3,7]
LHS = findLHS(nums)
print(LHS)
