
def containsDuplicate(nums):
    if sorted(set(nums)) == sorted(nums):
        return False
    return True

nums = [1,2,3,1]
hasDupe = containsDuplicate(nums)
print(hasDupe)
