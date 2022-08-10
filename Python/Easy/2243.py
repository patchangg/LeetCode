
def digitSum(s, k):

    while len(s) > k:
        groups = [s[i:i+k] for i in range(0, len(s), k)]
        s = ""
        for group in groups:
            s += str(sum([int(n) for n in group]))

    return s

s = "11111222223"
k = 3
roundSum = digitSum(s,k)
print(roundSum)
