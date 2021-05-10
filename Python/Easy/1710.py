
def maximumUnits(boxTypes, truckSize):
    maximum = 0
    limit = 0
    boxTypes.sort(key=lambda tup: tup[1])
    boxTypes.reverse()
    for i in boxTypes:
        if (i[0] + limit) < truckSize:
            maximum += i[0] * i[1]
            limit += i[0]
        else:
            maximum += (truckSize - limit ) * i[1]
            break
    return maximum



boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
maximum = maximumUnits(boxTypes,truckSize)
print(maximum)
