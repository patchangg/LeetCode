
def largestAltitude(gain):
    highest = 0
    altitude = gain[0]
    for i in range(1,len(gain)):
        altitude += gain[i]
        if altitude > highest:
            highest = altitude
    if highest <= 0:
        return 0
    else:
        return highest
# can just use max() for shorter loop
gain = [-4,-3,-2,-1,4,3,2]
highest = largestAltitude(gain)
print(highest)
