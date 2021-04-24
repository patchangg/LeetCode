
def countGoodRectangles(rectangles):
    small = 0
    count = 0
    for rectangle in rectangles:
        if min(rectangle) > small:
            count = 1
            small = min(rectangle)
        elif min(rectangle) == small:
            count += 1
    return count
        #print(rectangle)

rectangles = [[5,8],[3,9],[5,12],[16,5]]
count = countGoodRectangles(rectangles)
print(count)
