
def sumZero(n):
    upper,lower = divmod(n,2)
    isOdd = 0
    if lower == 0:
        num = n / 2
    else:
        num = n / 2 - 0.5
        isOdd = 1
    num = int(num)
    array = []
    while num > 0:
        array.append(num)
        array.append(-abs(num))
        num -= 1
    if isOdd == 1:
        array.append(0)
    return array

n = 5
sum = sumZero(n)
print(sum)
