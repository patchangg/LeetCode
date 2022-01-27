
def merge(self, intervals):
    intervals = sorted(intervals)
    output = [intervals[0]]
    for i in intervals:
        if i[0] <= output[-1][1]:
            output[-1][1] = max(output[-1][1],i[1])
        else:
            output.append(i)
    return output

# Sort the intervals from smallest to largest on the first element
# Put the first interval into an array
# Compare each interval, if the last element in the output array end is larger
# or equal to the start of the interval, if so find the larger end interval
# and replace the output array element with that, otherwise just append
# the interval as it's not overlapping the last element. O(nlogn), O(n) space
intervals = [[1,3],[2,6],[8,10],[15,18]]
nonOverlappingIntervals = merge(intervals)
print(nonOverlappingIntervals)
