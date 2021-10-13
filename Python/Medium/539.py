
def findMinDifference(timePoints):
    timePoints = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
    timePoints += [tp + 1440 for tp in timePoints]
    output = float('inf')
    for i in range(1,len(timePoints)):
        output = min(output,timePoints[i]-timePoints[i-1])
    return output

# Convert the timePoints into a integer and sort the array
# Add the time + 24 hours to create a circular time array to calculate
# the min times backwards and forwards.
# Compare the times and get the smallest difference
# O(nlogn), O(n) space
timePoints = ["23:59","00:00"]
minDifference = findMinDifference(timePoints)
print(minDifference)
