
def minFallingPathSum(matrix):
    for i in range(1,len(matrix)):
        for j in range(len(matrix[0])):
            if (j == 0):
                matrix[i][j] = min((matrix[i][j]+matrix[i-1][j]),(matrix[i][j]+matrix[i-1][j+1]))
            elif (j == len(matrix[0])-1):
                matrix[i][j] = min((matrix[i][j]+matrix[i-1][j-1]),(matrix[i][j]+matrix[i-1][j]))
            else:
                matrix[i][j] = min((matrix[i][j]+matrix[i-1][j-1]),(matrix[i][j]+matrix[i-1][j]),(matrix[i][j]+matrix[i-1][j+1]))
    return min(matrix[len(matrix)-1])

# DP question. Create a path from the top of the matrix to the bottom containing
# every possible combination of the values and get the smallest value of the row
# at the bottom of the matrix which should contain the values added previously.
# We replace matrix[i][j] with the smallest number from the row above it
# + the column above, next to it or the previous one.
# Have to get the edge cases where the column is either 0 or the last index
# O(N + M*N) where N is the amount of lists in the matrix
# M*N is the amount of numbers in each list * amount of lists in the matrix
# = O(N), O(1) space complexity 
matrix = [[2,1,3],[6,5,4],[7,8,9]]
minPath = minFallingPathSum(matrix)
print(minPath)
