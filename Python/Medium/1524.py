
def numOfSubarrays(arr):
    even = 0
    odd = 0
    output = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd, even = even, odd
            odd += 1
        output += odd
    return output % (10**9 + 7)

# Keep track of the even and odd numbers in the array
# If an even number appears, add one to even as it will create a new subarray
# If a odd number appears, swap the odd and even counters and add one to odd
# This is done as a odd + odd = even number so we need to flip them so the
# subarray remains odd. O(n), O(1) space
arr = [1,3,5]
oddSubarrays = numOfSubarrays(arr)
print(oddSubarrays)
