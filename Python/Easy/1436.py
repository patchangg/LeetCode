
def destCity(paths):
    dict = {}
    for i in paths:
        dict[i[0]] = 1
        if i[1] in dict:
            dict[i[1]] = 1
        else:
            dict[i[1]] = 0
    dest = [k for k,v in dict.items() if v == 0]
    return "".join(dest)

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
destination = destCity(paths)
print(destination)
