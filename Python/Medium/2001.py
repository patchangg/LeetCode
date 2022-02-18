
def interchangeableRectangles(rectangles):
    ratios = {}
    output = 0
    for rectangle in rectangles:
        division = rectangle[0]/rectangle[1]
        if division in ratios:
            output += ratios[division]
            ratios[division] += 1
        else:
            ratios[division] = 1
    return output

# Go through the array, store the width/height ratio in a hashmap, checking
# if any other rectangle had the same ratio. O(n), O(n) space
rectangles = [[4,8],[3,6],[10,20],[15,30]]
numRectangleRatios = interchangeableRectangles(rectangles)
print(numRectangleRatios)
