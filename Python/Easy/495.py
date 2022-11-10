
def findPoisonedDuration(timeSeries, duration):
    output = 0
    if len(timeSeries) == 0:
        return 0
    for i in range(1,len(timeSeries)):
        output += min(timeSeries[i] - timeSeries[i-1],duration)
    return output + duration

timeSeries = [1,4]
duration = 2
poisonDuration = findPoisonedDuration(timeSeries,duration)
print(poisonDuration)
