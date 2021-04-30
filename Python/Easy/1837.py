
def sumBase(n, k):
    digits = []
    sum = 0
    while n:
        digits.append(int(n % k))
        n //= k
    for i in digits[::-1]:
        sum += i
    return sum
    # answer = ""
    # while n > 0:
    #     answer = str(n%k) + answer
    #     n /= k
    # return answer

n = 34
k = 6
total = sumBase(n,k)
print(total)
