
def maximumScore(a, b, c:):
    output = 0
    while (a+b+c) > 1:
        if a > c and b >= c:
            output += 1
            a -= 1
            b -= 1
        elif a >= b and c > b:
            output += 1
            a -= 1
            c -= 1
        elif c >= a and b > a:
            output += 1
            b -= 1
            c -= 1
        elif a == b == c:
            output += 1
            a -= 1
            b -= 1
        if a == 0 and b == 0:
            break
        if a == 0 and c == 0:
            break
        if b == 0 and c == 0:
            break
    return output

# Brute force method of doing the question.
# O(n) average where n = a + b or c + b or b + c, O(1) space
a = 3
b = 8
c = 2
maximum = maximumScore(a,b,c)
print(maximum)
