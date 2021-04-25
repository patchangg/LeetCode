
def sortString(s):
    d = {}
    f = sorted(list(set(s)))
    for i in f:
        d[i] = s.count(i)
    sort = ''
    while d:
        temp = f[:]
        for i in f:
            sort = sort + i
            d[i] -= 1
            if d[i] == 0:
                d.pop(i)
                temp.remove(i)
        f = temp
        f.reverse()
    return sort

s = "aaaabbbbcccc"
sorted = sortString(s)
print(sorted)
