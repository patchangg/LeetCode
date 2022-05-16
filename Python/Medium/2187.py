
def minimumTime(time, totalTrips):
    left = min(time)
    right = totalTrips * min(time)
    while left < right:
        middle = (left + right) // 2
        numTrips = sum(middle // t for t in time)
        if numTrips < totalTrips:
            left = middle + 1
        else:
            right = middle
    return left

# Use binary search to find the minimumTime that would be used to get the minimum
# total trips. O(nlogn), O(1) space
time = [1,2,3]
totalTrips = 5
numTrips = minimumTime(time,totalTrips)
print(numTrips)
