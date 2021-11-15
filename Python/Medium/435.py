
def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x: x[1])
    n = len(intervals)
    output = 1
    if n == 0:
        return 0
    curr = intervals[0]

    for i in range(n):
        if curr[1] <= intervals[i][0]:
            output += 1
            curr = intervals[i]

    return n - output

# Sort the intervals by the end point then go through each point
# Count the number of non-overlapping intervals in the array by checking if
# the current invervals end point is less than or equal to the new intervals
# starting point. Once all the non-overlapping intervals are counted, remove
# the count from the number of intervals in the array to find the amount of
# overlapping intervals to be removed. O(nlogn), O(1) space
intervals = [[1,2],[2,3],[3,4],[1,3]]
intervalsRemoved = eraseOverlapIntervals(intervals)
print(intervalsRemoved)
