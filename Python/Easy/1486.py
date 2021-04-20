
def xorOperation(n, start):
    nums = []
    for i in range(n):
        nums.append(start + (2*i))
    xor = nums[0]
    for i in nums[1:]:
        xor ^= i
    return xor

n = 10
start = 5
xor = xorOperation(n,start)
print(xor)
