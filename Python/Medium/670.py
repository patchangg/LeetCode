
def maximumSwap(num):
    nums = [str(x) for x in str(num)]
    maximum = len(nums) - 1
    first = 0
    second = 0
    for i in range(len(nums)-1,-1,-1):
        if nums[i] > nums[maximum]:
            maximum = i
        if nums[i] < nums[maximum]:
            first = i
            second = maximum
    nums[first], nums[second] = nums[second], nums[first]

    return int("".join(nums))

# Change the number into a list of integers so we can swap them
# Going through the list backwards, record two integers to swap where the
# right integer is bigger than the left. This will find the largest integer
# in the array and swap it with the smallest integer position on the left,
# so once the swap occurs, the largest number occurs. O(n), O(n) space
num = 2736
maximumNumber = maximumSwap(num)
print(maximumNumber)
