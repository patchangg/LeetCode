
def addStrings(num1, num2):
    num1 = list(num1)
    num2 = list(num2)
    output = []
    carry = 0

    while len(num1) > 0 or len(num2) > 0:
        n1 = 0
        n2 = 0
        if len(num1) > 0:
            n1 = ord(num1.pop()) - ord('0')
        if len(num2) > 0:
            n2 = ord(num2.pop()) - ord('0')
        temp = n1 + n2 + carry
        output.append(temp % 10)
        carry = temp // 10
    if carry:
        output.append(carry)
    return "".join([str(i) for i in output])[::-1]

num1 = "11"
num2 = "123"
addNums = addStrings(num1,num2)
print(addNums)
