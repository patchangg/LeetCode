
def getMaximumXor(nums, maximumBit):
    power = 2 ** maximumBit - 1
    output = []
    xor = 0
    for num in nums:
        xor ^= num
        print(xor, power, xor ^ power)
        output.append(xor ^ power)
    output.reverse()
    return output


nums = [0,1,1,3]
maximumBit = 2
maximum = getMaximumXor(nums,maximumBit)
print(maximum)

    # power = 2 ** maximumBit
    # output = []
    # while nums:
    #     xor = nums[0]
    #     maximum = 0
    #     index = 0
    #     if len(nums) > 1:
    #         for i in range(1,len(nums)):
    #             xor ^= nums[i]
    #     for s in range(power):
    #         if (xor ^ s) > maximum:
    #             maximum = (xor ^ s)
    #             index = s
    #     output.append(index)
    #     nums.pop()
    # return output
