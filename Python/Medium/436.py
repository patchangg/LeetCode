from bisect import bisect_left

def findRightInterval(intervals):
    intervs = sorted([[j,k,i] for i,[j,k] in enumerate(intervals)])
    output = [-1] * len(intervals)
    for i,j,k in intervs:
        interval = bisect_left(intervs,[j])
        if interval < len(intervals):
            output[k] = intervs[interval][2]
    return output

# Sort the intervals based on the start interval and add the oringal index
# position with it. For each interval, check if there is a position it can
# move itself to that the start is less than another start and since the
# array is sorted, the gap is minimised. If the position is out of bounds, then
# don't update the output array. O(nlogn), O(n) space
intervals = [[3,4],[2,3],[1,2]]
rightIntervals = findRightInterval(intervals)
print(rightIntervals)
