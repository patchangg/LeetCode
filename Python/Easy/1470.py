nums = [2,5,1,3,4,7]
n = 3
def shuffle(self, nums, n):
    shuffle = []
    a = nums[:n]
    b = nums[n:]
    i = 0
    while i < n:
        shuffle.append(a[i])
        shuffle.append(b[i])
        i += 1
    return shuffle

shuffle(nums,n)
