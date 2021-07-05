from collections import defaultdict

def restoreArray(adjacentPairs):
    def dfs(u):
        output.append(u)
        visited.add(u)
        for v in dicts[u]:
            if v not in visited:
                dfs(v)
    dicts = defaultdict(list)
    for u,v in adjacentPairs:
        dicts[u].append(v)
        dicts[v].append(u)
    edges = [x for x in dicts if len(dicts[x]) == 1]
    visited = set()
    output = []
    dfs(edges[0])
    return output

# Find the number that only appears once in the adjacentPairs.
# This will be the start of the array.
# Do a DFS search on the pairs to find the order of the array.
# O(n + 2*n) = O(3n) = O(n) where n is length of adjacentPairs and
# 2*n is the pairs that the DFS has to search through. 
adjacentPairs = [[2,1],[3,4],[3,2]]
restoredArray = restoreArray(adjacentPairs)
print(restoreArray)
