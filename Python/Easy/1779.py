
def nearestValidPoint(x, y, points):
    output = []
    smallest = -1
    for point in points:
        if point[0] == x or point[1] == y:
            if smallest == -1:
                smallest = (abs(x-point[0]) + abs(y-point[1]))
            if (abs(x-point[0]) + abs(y-point[1])) < smallest:
                output = [points.index(point)]
                smallest = (abs(x-point[0]) + abs(y-point[1]))
            elif (abs(x-point[0]) + abs(y-point[1])) == smallest:
                output.append(points.index(point))
    if output:
        return output[0]
    else:
        return -1



x = 28
y = 51
points = [[25,45],[60,19],[11,38],[32,22],[1,24],[26,25],[52,36],[45,54],[45,30],[45,39],[39,38],[25,38],[39,57],[47,51],[47,49],[37,21],[16,43],[53,33],[10,50],[30,29],[3,31],[45,26],[22,40],[2,31],[57,42],[25,42],[37,13],[13,54],[17,5],[50,32]]
valid = nearestValidPoint(x,y,points)
print(valid)
