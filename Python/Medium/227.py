
def calculate(s):
    output = []
    sign = "+"
    num = 0
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if s[i] in "+-*/" or i == len(s) - 1:
            if sign == "+":
                output.append(num)
            elif sign == "-":
                output.append(-num)
            elif sign == "*":
                output.append(output.pop()*num)
            else:
                output.append(int(output.pop()/num))
            num = 0
            sign = s[i]
    return sum(output)

# Use a stack to store the numbers from the string.
# If a digit is found, multiply the previous digit/number found by 10 and
# add the digit to it.
# Once a sign is found, use the previous sign to calculate what to do and
# store the current sign for the next number
# O(n), O(n) space
s = "3+2*2"
total = calculate(s)
print(total)
