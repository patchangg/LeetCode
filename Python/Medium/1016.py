
def queryString(self, s: str, n: int) -> bool:
    for i in range(n,0,-1):
        if bin(i)[2:] not in s:
            return False
    return True

# Check every binary representation from n to 0 is in n
# O(slogn), O(s) space
