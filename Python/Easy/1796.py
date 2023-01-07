
def secondHighest(s):
    nums = set()
    for c in s:
        if c.isnumeric():
            nums.add(c)
    if len(nums) > 1:
        nums = sorted(nums)
        return int(nums[-2])
    else:
        return -1

s = "dfa12321afd"
secondLargestNum = secondHighest(s)
print(secondLargestNum)
