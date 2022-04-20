
def maximumCandies(candies, k):
    left = 0
    right = sum(candies) // k
    while left < right:
        middle = (left + right + 1) // 2
        if k > sum(c // middle for c in candies):
            right = middle - 1
        else:
            left = middle
    return left

# Binary search to find the maximum amount of candies to give to each person
# by using the sum of the candies divided by the amount of people as the maximum size
# Reduce the size until there is no more numbers greater than the maximum that
# can be given to k people. O(nlogn), O(1) space
candies = [5,8,6]
k = 3
numCandies = maximumCandies(candies,k)
print(numCandies)
