
def maxArea(sheight):
    i = 0
    j = len(height) - 1
    water = 0
    while i < j:
        water = max(water, (j - i) * min(height[j],height[i]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return water

# Sliding window to check the maximum area between two heights that will
# contain water. Slide the slide with the lowest height until i > j.
# If the scenario height[i] == height[j], we remove the height from the right
# side as either side will most likely contain a smaller area than the current
# O(n), O(1) space
height = [1,8,6,2,5,4,8,3,7]
mostWater = maxArea(height)
print(mostWater)
