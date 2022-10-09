
def findLUSlength(self, a: str, b: str) -> int:
    if a == b:
        return -1
    return max(len(a), len(b))

a = "aba"
b = "cdc"
lusLength = findLUSlength(a,b)
print(lusLength)
