
def frequencySort(nums):
    dict = {}
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    xs = sorted(sorted(nums, reverse=True), key=lambda x: dict[x])
    return(xs)


nums = [-1,1,-6,4,5,-6,1,4,1]
freq = frequencySort(nums)
print(freq)
