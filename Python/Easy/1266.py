
def minTimeToVisitAllPoints(points):
    length = len(points) - 1
    previousx = points[0][0]
    previousy = points[0][1]
    seconds = 0
    i = 1
    while i <= length:
        movex = abs(points[i][0] - previousx)
        movey = abs(points[i][1] - previousy)
        previousx = points[i][0]
        previousy = points[i][1]
        while movex > 0 or movey > 0:
            if movex >= 1 and movey >= 1:
                seconds += 1
                movex -= 1
                movey -= 1
            elif movex >= 1 and movey <= 0:
                movex -= 1
                seconds += 1
            elif movey >= 1 and movex <= 0:
                movey -= 1
                seconds += 1
        i += 1
    return seconds


points = [[1,1],[3,4],[-1,0]]
min = minTimeToVisitAllPoints(points)
print(min)
