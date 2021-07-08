
def numTimesAllBlue(light):
    on = output = hi = 0
    for l in light:
        on += 1
        if l>hi:
            hi = l
        if on == hi:
            output += 1
    return output

# Get the maximum number while traversing the array and compare to the
# amount of lights on. If high == on that means all lights to the left of
# high must be on therefore add one to the result
# O(n), O(1) space
light = [3,2,4,1,5]
number = numTimesAllBlue(light)
print(number)
