
def flipAndInvertImage(image):
    array = []
    for i in image:
        num = []
        for s in reversed(i):
            if s == 0:
                num.append(1)
            elif s == 1:
                num.append(0)
        array.append(num)
    return array


image = [[1,1,0],[1,0,1],[0,0,0]]
flipped = flipAndInvertImage(image)
print(flipped)
