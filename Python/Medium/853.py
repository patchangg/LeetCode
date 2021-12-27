
def carFleet(target, position, speed):
    times = [float(target-p) / s for p,s in sorted(zip(position,speed))]
    output = 0
    leader = 0
    for time in times[::-1]:
        if time > leader:
            output += 1
            leader = time
    return output

# Sort each car and find out how long it will take to get to to the target.
# Loop through the times and record the new slowest time to get to the
# target, which will become the leader of the new car fleet, if the time is less
# than the current leader, that means it will catch up to the leader and be
# part of their fleet. O(nlogn), O(n) space
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
numCarFleets = carFleet(target,position,speed)
