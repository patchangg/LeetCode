
def decompressRLElist(nums):
    i = len(nums)
    s = 0
    list = []
    while s < i: # can do for i in range(0,len(nums),2)
        freq = nums[s]
        val = nums[s+1]
        for j in range(freq):
             list.append(val)
        s += 2
    return list

nums = [1,1,2,3]
list = decompressRLElist(nums)
print(list)
