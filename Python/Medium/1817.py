
def findingUsersActiveMinutes(logs, k):
    output = [0 for i in range(k)]
    dict = {}
    for i in logs:
        if i[0] not in dict:
            dict[i[0]] = [i[1]]
        else:
            list = dict[i[0]]
            if i[1] not in list:
                dict[i[0]].append(i[1])
    for key,value in dict.items():
        output[len(value)-1] += 1
    return output


logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
uam = findingUsersActiveMinutes(logs,k)
print(uam)
