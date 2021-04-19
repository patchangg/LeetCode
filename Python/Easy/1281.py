import math
def subtractProductAndSum(n):
    s = str(n)
    digits = int(math.log10(n))+1
    product = 1
    addition = 0
    for i in range(digits):
        product *= int(s[i])
        addition += int(s[i])
    sum = product - addition
    return sum


n = 4421
s = subtractProductAndSum(n)
print(n)
# non import math way is to do len(str(n))
