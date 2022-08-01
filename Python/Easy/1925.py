from math import sqrt

def countTriples(n):
    output = 0

    for i in range(1, n):
        for j in range(i+1, n):
            s = sqrt(i**2 + j**2)
            if int(s) == s and s <= n:
                output += 2
    return output

n = 5
tripleSquares = countTriples(n)
print(tripleSquares)
