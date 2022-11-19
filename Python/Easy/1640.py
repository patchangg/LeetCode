
def canFormArray(arr, pieces):
    output = []
    for i in range(len(arr)):
        for j in range(len(pieces)):
            if arr[i] == pieces[j][0]:
                for k in range(len(pieces[j])):
                    output.append(pieces[j][k])
    return output == arr

arr = [15,88]
pieces = [[88],[15]]
canMakeArrFromPieces = canFormArray(arr,pieces)
print(canMakeArrFromPieces)
