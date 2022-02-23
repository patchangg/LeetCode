
def strWithout3a3b(self, a: int, b: int) -> str:
    output = []
    while a + b > 0:
        if output[-2:] == ['a','a']:
            output.append('b')
            b -= 1
        elif output[-2:] == ['b','b']:
            output.append('a')
            a -= 1
        elif a >= b:
            output.append('a')
            a -= 1
        elif b:
            output.append('b')
            b -= 1
    return "".join(output)

# If the last two letters are the same, add the opposite letter.
# If there is more a than b, take a first. O(n), O(n) space
a = 1
b = 2
noThreeAorBString = strWithout3a3b(a,b)
print(noThreeAorBString)
