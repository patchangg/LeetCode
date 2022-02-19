
def addRungs(rungs, dist):
    output = 0
    prev = 0
    for rung in rungs:
        output += ((rung - prev - 1) // dist)
        prev = rung
    return output

# Loop through the array, check the distance between the current rung and the
# previous to calculate if any rung is needed. If a rung is needed,
# divide the gap by dist to add how many is needed to the output.
# O(n), O(1) space
rungs = [1,3,5,10]
dist = 2
addedRungs = addRungs(rungs,dist)
print(addedRungs)
