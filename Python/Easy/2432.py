
def hardestWorker(n, logs):
    emp = [logs[0][0]]
    longest = logs[0][1]
    for i in range(1,len(logs)):
        e = logs[i][0]
        time = logs[i][1] - logs[i-1][1]
        if time > longest:
            emp = [e]
            longest = time
        elif time == longest:
            emp.append(e)
    return min(emp)

n = 10
logs = [[0,3],[2,5],[0,9],[1,15]]
employeeOnLongestTask = hardestWorker(n,logs)
print(employeeOnLongestTask)
