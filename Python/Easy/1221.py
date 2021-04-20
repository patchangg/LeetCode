
def balancedStringSplit(s):
    count = 0
    balanced = 0
    for i in s:
        if i == "R":
            count += 1
        elif i == "L":
            count -= 1

        if count == 0:
            balanced += 1
    return balanced

s = "RLLLLRRRLR"
balanced = balancedStringSplit(s)
print(balanced)
