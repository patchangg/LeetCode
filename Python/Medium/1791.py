
def findCenter(edges):
    dict = {}
    for edge in edges:
        if edge[0] in dict:
            dict[edge[0]] += 1
        else:
            dict[edge[0]] = 1
        if edge[1] in dict:
            dict[edge[1]] += 1
        else:
            dict[edge[1]] = 1
    return max(dict, key=dict.get)

edges = [[1,2],[5,1],[1,3],[1,4]]
center = findCenter(edges)
print(center)
