
def integerReplacement(self, n: int) -> int:
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + self.integerReplacement(n/2)
    else:
        return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))

# Use recursion to find out how many steps it takes to get from n to 1. O(1) space
n = 8
stepsToOne = integerReplacement(n)
print(stepsToOne)
