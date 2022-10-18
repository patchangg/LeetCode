
def getRow(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        temp = []
        for x, y in zip([0]+row, row+[0]):
            temp.append(x+y)
        row = temp
    return row

rowIndex = 3
rowNums = getRow(rowIndex)
print(rowNums)
