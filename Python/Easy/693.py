
def hasAlternatingBits(n):
    bits = str(bin(n)[2:])
    prev = bits[0]
    for i in range(1,len(str(bits))):
        if prev == bits[i]:
            return False
        prev = bits[i]
    return True

n = 5
alternatingBits = hasAlternatingBits(n)
print(alternatingBits)
