from bisect import bisect

def numFriendRequests(ages):
    output = 0
    ages = sorted(ages)
    for i in range(len(ages)):
        age = ages[i]
        right = bisect(ages,age)
        left = bisect(ages,0.5*age+7)
        output += max(0,right-left-1)
    return output

# Sort the ages and find the upper and lower bound that x would send a friend
# request to. For each age, the ages between ages that is 1 below it to
# 0.5 * age + 7, that age will send a friend request to. Using the index location
# for the upper - lower bound will the num friend requests.
# The rule age[y] > 100 && age[x] < 100 will never apply as rule 2
# age[y] > age[x] is overwrites it. O(nlogn), O(n) space
ages = [16,16]
numFriendsR = numFriendsRequests(ages)
print(numFriendsR)
