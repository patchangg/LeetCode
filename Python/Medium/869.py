
def reorderedPowerOf2(n):
    powers = ["".join(sorted(list(str(1<<i)))) for i in range(30)]
    target = "".join(sorted(list(str(n))))
    return target in powers

# Create an array of powers of two using bitwise shift to get up to 10^9
# Sort the input and the power array so that we can compare them
# if the sorted input is in the powers array then return true, else false
# O(30+n) = O(n), O(1) space
n = 46
poweroftwo = reorderedPowerOf2(n)
print(poweroftwo)
