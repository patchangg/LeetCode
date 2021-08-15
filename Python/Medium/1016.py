
def queryString(s, n):
    for i in range(n,0,-1):
        if bin(i)[2:] not in s:
            return False
    return True

s = "0110"
n = 3
query = queryString(s,n)
print(query)
# Check every binary representation from n to 0 is in n
# O(slogn), O(s) space
