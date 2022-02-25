
def increasingTriplet(nums):
    i = float(inf)
    j = float(inf)
    for num in nums:
        if num <= i:
            i = num
        elif num <= j:
            j = num
        else:
            return True
    return False

# Go through the array, recording and resetting the smallest number once found,
# then look for a number greater than the smallest number after and recording that
# and if a another greater number is found that means an increasing triplet
# is found. O(n), O(1) space
nums = [1,2,3,4,5]
triplet = increasingTriplet(nums)
print(triplet)
