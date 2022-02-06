
def reconstructMatrix(upper, lower, colsum):
    upperRow = [0] * len(colsum)
    lowerRow = [0] * len(colsum)

    for i,num in enumerate(colsum):
        if num == 1:
            if upper > lower:
                upperRow[i] = 1
                upper -= 1
            else:
                lowerRow[i] = 1
                lower -= 1
        elif num == 2:
            upperRow[i] = 1
            lowerRow[i] = 1
            upper -= 1
            lower -= 1

    if upper == 0 and lower == 0:
        return [upperRow, lowerRow]
    else:
        return []

# The upper and lower row must be equal to the length of the colsum
# Go through the colsum, if 2 appears, both upper and lower array positions
# equals one, if 1 appears, use the row that has the most sum remaining.
# If both upper and lower equal 0 at the end, the solution will be valid.
# O(n), O(n) space
upper = 2
lower = 1
colsum = [1,1,1]
binaryMatrix = reconstructMatrix(upper,lower,colsum)
print(binaryMatrix)
