
def heightChecker(heights):
    sorted = heights.copy()
    sorted.sort()
    incorrect = 0
    for i in range(len(heights)):
        if sorted[i] != heights[i]:
            incorrect += 1
    return incorrect


heights = [1,1,4,2,1,3]
checker = heightChecker(heights)
print(checker)
