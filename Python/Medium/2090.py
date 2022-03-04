
def getAverages(nums, k):
    output = [-1] * len(nums)
    left = 0
    curr = 0
    window = k*2+1

    for right in range(len(nums)):
        curr += nums[right]
        if (right-left+1 >= window):
            output[left+k] = curr // window
            curr -= nums[left]
            left += 1
    return output

# Create a sliding window size k * 2 + 1. Once the window size has been met,
# store the average of the window in the middle of the window or left + k
# O(n), O(n) space
nums = [7,4,3,9,1,8,5,2,6]
k = 3
windowAverage = getAverages(nums,k)
print(windowAverage)
