
def eliminateMaximum(dist, speed):
    arrival = []
    for d, s in zip(dist,speed):
        arrival.append((d-1) // s)
    for i, t in enumerate(sorted(arrival)):
        if i > t:
            return i
    return len(dist)

# Create an array that has the arrival time of each monster.
# Loop through the arrival times sorted, if they arrive before the index
# they arrive at, return the index as that is the maximum amount of monsters
# that can be killed as it arrives during another monster attack.
# O(nlogn), O(n) space
dist = [1,3,4]
speed = [1,1,1]
monstersKilled = eliminateMaximum(dist,speed)
print(monstersKilled)
