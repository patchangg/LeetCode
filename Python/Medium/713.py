
def numSubarrayProductLessThanK(nums, k):
    l = 0
    product = 1
    output = 0

    for r in range(len(nums)):
        product *= nums[r]

        while product >= k and l <= r:
            product /= nums[l]
            l += 1

        output += (r + 1 - l)
    return output

# Use two pointers to create a sliding window which has a product that is less
# than k. If the product is greater than k, move the left pointer forward.
# Right - Left + 1 is the amount of subarrays that can be created with the
# numbers in the window that is less than k. O(n), O(1) space
nums = [10,5,2,6]
k = 100
numSubarraysLessThanK = numSubarrayProductLessThanK(nums,k)
print(numSubarraysLessThanK)
