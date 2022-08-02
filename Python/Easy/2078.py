
def maxDistance(colors):
    i = 0
    j = len(colors) - 1
    while colors[0] == colors[j]:
        j -= 1
    while colors[i] == colors[-1]:
        i += 1
    return max(len(colors) - 1 - i, j)

colors = [1,1,1,6,1,1,1]
maximumDistance = maxDistance(colors)
print(maximumDistance)
