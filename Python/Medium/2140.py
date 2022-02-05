
def mostPoints(questions):
    dp = [0] * (len(questions) + 1)
    for i in range(len(questions) - 1, -1, -1):
        points = questions[i][0]
        skip = questions[i][1]
        dp[i] = max(points + dp[min(skip + i + 1, len(questions))], dp[i + 1])
    return dp[0]

# To find the most points able to be gained from the first question, calculate
# the maximum points you can get starting from every question in the array
# so that the first question will contain the path to maximise the points
# To calculate the points, each question will store the points from either
# skipping the question or answering it. O(n), O(n) space
questions = [[3,2],[4,3],[4,4],[2,5]]
maximumPoints = mostPoints(questions)
print(maximumPoints)
