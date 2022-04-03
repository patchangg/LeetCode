
def numberOfWeeks(milestones):
    maximum = -1
    total = 0

    for i in range(len(milestones)):
        maximum = max(maximum,milestones[i])
        total += milestones[i]

    diff = total - maximum

    if maximum - diff > 1:
        return total - (maximum - diff - 1)
    else:
        return total

# Find the maximum number and total sum of the milestones.
# Get the difference between the total and maximum. If the maximum minus
# the difference is greater than one, that means all milestones cannot be
# finished so return the maximum target achieved
# otherwise return the total sum. O(n), O(1) space
milestones = [1,2,3]
numWeeks = numberOfWeeks(milestones)
print(numWeeks)
