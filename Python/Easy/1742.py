
def countBalls(lowLimit, highLimit):
    dict = {}
    for i in range(lowLimit,highLimit+1):
        sum = 0
        l = list(str(i))
        for s in l:
            sum += int(s)
        if sum in dict:
            dict[sum] += 1
        else:
            dict[sum] = 1
    max = 0
    for key in dict:
        if dict[key] > max:
            max = dict[key]
    return max



lowLimit = 19
highLimit = 28
counted = countBalls(lowLimit,highLimit)
print(counted)
