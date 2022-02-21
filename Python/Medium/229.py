from collections import Counter

def majorityElement(nums):
    counted = Counter(nums)
    output = []
    for num,val in counted.most_common():
        if val > (len(nums) // 3):
            output.append(num)
    return output

# Count the occurances of each integer in the array.
# For each integer that occurs more than n/3 times, append it to the array
# O(nlogn), O(n) space
nums = [3,2,3]
majorityElements = majorityElement(nums)
print(majorityElements)
