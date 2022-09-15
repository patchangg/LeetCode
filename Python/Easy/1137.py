
def tribonacci(n):
    nums = [0,1,1]
    for i in range(3,n+1):
        nums.append(nums[-3] + nums[-2] + nums[-1])
    if n < 3:
        return nums[n]
    else:
        return nums[-1]

n = 4
tribo = tribonacci(n)
print(tribo)
