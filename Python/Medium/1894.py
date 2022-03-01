
def chalkReplacer(chalk, k):
    k %= sum(chalk)

    for i, usage in enumerate(chalk):
        if k < usage:
            return i
        k -= usage
    return 0

# Mod k with the sum of the chalk to get the remainder.
# Go through the students and minus their chalk usage. When a student has less
# than 0 chalk after using it, return that student index otherwise keep removing
# chalk usage from k. O(n), O(1) space
chalk = [5,1,5]
k = 22
student = chalkReplacer(chalk,k)
print(student)
