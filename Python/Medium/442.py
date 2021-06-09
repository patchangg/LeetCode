
def findDuplicates(nums):
    seen = set()
    seenadd = seen.add
    dup = set( x for x in nums if x in seen or seenadd(x) )
    return list(dup)

#seenadd is a faster method of adding to a set as its called "hoisting"
# hoisting is using bounding a attribute to the set so it calls it faster
nums = [4,3,2,7,8,2,3,1]
dups = findDuplicates(nums)
print(dups)
