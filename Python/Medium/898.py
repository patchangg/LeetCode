
def subarrayBitwiseORs(arr):
    res = set(arr)
    prev = set()
    prev.add(arr[0])
    for num in arr:
        curr = set()
        for p in prev:
            curr.add(num | p)
            res.add(num | p)
        prev = curr
        prev.add(num)
    return len(res)

# Create a set to remove dupliate numebrs.
# Go through the array, bitwise or the number with the other known numbers
# and record and new non-duplicate numbers. Return the length of the
# results. O(n), O(n) space
arr = [0]
subarrays = subarrayBitwiseORs(arr)
print(subarrays)
