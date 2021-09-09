
def minDifference(nums):
    if len(nums) <= 4:
        return 0
    nums = sorted(nums)
    output = []
    for a, b in zip(nums[:4], nums[-4:]):
        output.append(b-a)
    return min(output)

# Have to find the minimum difference after at most 3 changes to the array
# There are 4 scenarios we need to do, remove three largest, three smallest,
# 2 largest + smallest and 2 smallest + largest to find the optimal minimal
# difference. We use the numbers that are newest minimum and maximum to get
# the minimal difference. After the scenarios, return the smallest difference
nums = [82,81,94,75,20]
minimumDif = minDifference(nums)
print(minimumDif)
