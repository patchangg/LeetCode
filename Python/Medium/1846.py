
def maximumElementAfterDecrementingAndRearranging(arr):
    arr = sorted(arr)
    prev = 0
    for num in arr:
        prev = min(num,prev+1)
    return prev

# Sort the array so that 1 will be in the first position
# Every index has to be less than or equal to 1
# So we check current if it is smaller or equal to the previous + 1
# and get the smallest integer. This will minimise the array and the last
# element will contain the largest possible number
# O(nlogn), O(n) space
arr = [2,2,1,2,1]
maximisedArray = maximumElementAfterDecrementingAndRearranging(arr)
print(maximisedArray)
