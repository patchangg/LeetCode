
def maxScore(cardPoints, k):
    front = [0]
    back = [0]
    for points in cardPoints:
        front.append(front[-1] + points)
    for points in cardPoints[::-1]:
        back.append(back[-1] + points)
    output = [front[i] + back[k-i] for i in range(k + 1)]
    return max(output)

# Get the culumative sum for the points from the front and the back
# Calculate every possible combination and return the largest combination
# sum. O(2n + k), O(n) space
cardPoints = [1,2,3,4,5,6,1]
k = 3
maximumScore = maxScore(cardPoints,k)
print(maximumScore)
