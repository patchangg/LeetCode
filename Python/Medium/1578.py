
def minCost(s, cost):
    left = 0
    output = 0
    for right in range(1,len(cost)):
        if s[left] == s[right]:
            if cost[left] < cost[right]:
                output += cost[left]
            else:
                output += cost[right]
                continue
        left = right
    return output

# Want to check if the two characters in s are the same
# if so add the smallest cost to the output to keep
# if the right index is cheaper, we delete the right so we have
# a index stronger to compare to the next if it is duplicate
# O(n), O(1)
s = "aabaa"
cost = [1,2,3,4,1]
minimum = minCost(s,cost)
print(minimum)
