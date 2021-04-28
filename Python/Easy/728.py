
def selfDividingNumbers(left, right):
    dividing = []
    for i in range(left,right+1):
        lists = list(str(i))
        dividable = True
        for s in lists:
            if int(s) != 0:
                if (i % int(s)) != 0:
                    dividable = False
            else:
                dividable = False
        #print(i,dividable)
        if dividable:
            dividing.append(i)
    return dividing

left = 1
right = 22
selfDividing = selfDividingNumbers(left,right)
print(selfDividing)
