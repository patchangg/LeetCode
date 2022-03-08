
def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = abs(ax2-ax1) * abs(ay2-ay1)
    area2 = abs(bx2-bx1) * abs(by2-by1)
    width = min(ax2,bx2) - max(ax1,bx1)
    height = min(ay2, by2) - max(ay1,by1)
    if width <= 0 or height <= 0:
        return area1 + area2
    else:
        return area1 + area2 - width * height

# Calculate the area of the two rectangles and get the total width and height
# of both rectangles combined. If the width or height is not positive, it means
# they do not overlap so return the sum of both areas otherwise calculate
# the width * height + both areas and return it. O(1), O(1) space
ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
totalArea = computeArea(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2)
print(totalArea)
