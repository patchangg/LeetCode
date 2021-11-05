
def subsetsWithDup(nums):
    output = [[]]
    nums = sorted(nums)
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            l = len(output)
            for j in range(len(output)):
                output.append(output[j] + [nums[i]])
        else:
            k = len(output)
            for j in range(l,len(output)):
                output.append(output[j] + [nums[i]])
            l = k
        print(output)
    return output

# Sort the nums array and then loop through it.
# If the current integer is 0 or not the same as the previous integer, that means
# it is a new number, so we create combinations of every other subarrays that
# came before it.
# If the current integer is the same as the previous integer, we just append
# the integer from where the previous new number started to not make any
# duplicates in the array. O(n), O(n) space
nums = [1,2,2]
powerSet = subsetsWithDup(nums)
print(powerSet)
