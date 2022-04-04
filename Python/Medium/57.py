
def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals = sorted(intervals)
    output = [intervals[0]]
    for i in intervals:
        if i[0] <= output[-1][1]:
            output[-1][1] = max(output[-1][1],i[1])
        else:
            output.append(i)
    return output

# Add the new interval into the array and sort based off the start time.
# Add the new interval if the start time does not match the old start time
# otherwise compare the start and end time of the new and oldest interval in
# the updated array and change it to the maximum. O(nlogn), O(n) space
intervals = [[1,3],[6,9]]
newInterval = [2,5]
updatedInterval = insert(intervals,newInterval)
print(updatedInterval)
