
def getMaxLen(nums):
    pos = 0
    neg = 0
    output = 0
    for num in nums:
        if num == 0:
            pos = 0
            neg = 0
        elif num > 0:
            pos += 1
            if neg > 0:
                neg += 1
            else:
                neg = 0
        else:
            if neg > 0:
                pos, neg = neg + 1, pos + 1
            else:
                pos, neg = 0, pos + 1
        output = max(output,pos)
    return output

# Go through the numbers array. If 0 appears, reset positive and negative.
# Otherwise, count the amount of positives and negatives seen.
# Keep track of the number of positive and negative numbers. If the product
# sum is positive and a negative number is next, flip the positive and negative
# total count, vice versa for negative number with another neagtive.
# Each loop, compare the total positive length to find a new maximum length.
# O(n), O(1) space
nums = [1,-2,-3,4]
maxLength = getMaxLen(nums)
print(maxLength)
