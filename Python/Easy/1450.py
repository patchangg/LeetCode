
def busyStudent(startTime, endTime, queryTime):
    length = len(startTime)
    busy = 0
    for i in range(length):
        if startTime[i] <= queryTime and endTime[i] >= queryTime:
            busy += 1
    return busy


startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
query = busyStudent(startTime,endTime,queryTime)
print(query)
