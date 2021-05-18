
def groupThePeople(groupSizes):
    dicts = {}
    for i in range(len(groupSizes)):
        if groupSizes[i] not in dicts:
            dicts[groupSizes[i]] = [i]
        else:
            num = groupSizes[i]
            dicts[num].append(i)
    output = []
    for key,value in dicts.items():
        group = []
        count = 0
        for i in value:
            group.append(i)
            count += 1
            if count == key:
                count = 0
                output.append(group)
                group = []
    return output

groupSizes = [3,3,3,3,3,1,3]
grouped = groupThePeople(groupSizes)
print(grouped)
