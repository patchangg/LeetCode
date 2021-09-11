from collections import Counter

def isPossibleDivide(nums, k):
    counted = Counter(nums)
    for i in sorted(counted):
        if counted[i] > 0:
            for j in range(k)[::-1]:
                counted[i+j] -= counted[i]
                if counted[i+j] < 0:
                    return False
    return True

# Count the numbers in the array
# Loop through the Counter and check if k number ahead has the same amount or
# more count than the integer so that we can divide the array into sets of k
# If it doesn't than that means we can't split the array so return False
# Do this for every number and return True.
# O(nlogn + n*k), O(n) space
nums = [1,2,3,3,4,4,5,6]
k = 4
isPossible = isPossibleDivide(nums,k)
print(isPossible)
