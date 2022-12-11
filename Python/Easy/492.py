
def constructRectangle(area):
    for l in range(int(math.sqrt(area)),0,-1):
        if area % l == 0:
            return [area // l , l]

area = 4
rectangleArea = constructRectangle(area)
print(rectangleArea)
