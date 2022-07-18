
def luckyNumbers(matrix):
    minR = [float(inf)] * len(matrix)
    maxC = [1] * len(matrix[0])
    output = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            maxC[col] = max(matrix[row][col],maxC[col])
        minR[row] = min(min(matrix[row]),minR[row])
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if minR[row] == matrix[row][col] and maxC[col] == matrix[row][col]:
                output.append(matrix[row][col])
    return output

matrix = [[3,7,8],[9,11,13],[15,16,17]]
luckyNums = luckyNumbers(matrix)
print(luckyNums)
