
def findBestValue(arr, target):
    arr = sorted(arr)
    total = 0
    n = len(arr)

    for i in range(n):
        output = round((target - total) / n)
        if output < arr[i]:
            return output
        total += arr[i]
        n -= 1

    return arr[-1]

# Sort the array and go through it.
# Each loop, check if the sum of the array if changed to the current index
# integer would be less than the target. Since we want minimum integer in case
# of a tie, the sorted array will ensure that is true.
# If this is impossible, return the largest number as that would get the
# number closest to the target. O(nlogn), O(1) space
arr = [4,9,3]
target = 10
bestValue = findBestValue(arr,target)
print(bestValue)
