
def sortByBits(arr):
    dict = {}
    for num in arr:
        binary = "{0:#b}".format(num)
        oneAmount = binary.count("1")
        if oneAmount not in dict:
            dict.setdefault(oneAmount,[])
            dict[oneAmount].append(num)
        else:
            dict[oneAmount].append(num)
    print(dict)
    final = []
    for key,value in sorted(dict.items()):
        value.sort()
        for i in value:
            final.append(i)
    return final
    #dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
    #return list(dict.keys())

#arr = [10,100,1000,10000]
#arr = [0,1,2,3,4,5,6,7,8]
arr = [1024,512,256,128,64,32,16,8,4,2,1]
sorted = sortByBits(arr)
print(sorted)
