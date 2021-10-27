
def prevPermOpt1(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] <= arr[i+1]:
        i -= 1
    if i >= 0:
        highest = i + 1
        for j in range(highest+1,len(arr)):
            if arr[highest] < arr[j] < arr[i]:
                highest = j
        arr[highest],arr[i] = arr[i],arr[highest]
    return arr

# Find the largest number from right to left to maximise the permutation
# If i is less than 0, that means the array is already in its largest state
# If i is greater or equal to 0, we now find the second largest number on the right
# side of the largest number to swap with. Once we look through the right side,
# swap the second largeset with the largest number to get the largest permutation
# O(n), O(1) space
arr = [3,2,1]
largestPermutation = prevPermOpt1(arr)
print(largestPermutation)
