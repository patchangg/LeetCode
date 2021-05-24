
def checkArithmeticSubarrays(nums, l, r):
    output = []
    for i in range(len(l)):
        arr = nums[l[i]:r[i]+1]
        arr.sort()
        diff = arr[1] - arr[0]
        okay = True
        for s in range(1,len(arr)):
            if (arr[s] - arr[s-1]) != diff:
                okay = False
        output.append(okay)
    return output

# nums = [4,6,5,9,3,7]
# l = [0,0,2]
# r = [2,3,5]
nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]
isArithmetic = checkArithmeticSubarrays(nums,l,r)
print(isArithmetic)
