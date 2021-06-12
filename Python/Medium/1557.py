
def findSmallestSetOfVertices(n, edges):
    return list(set(range(n)) - set(j for i, j in edges))

# find all the nodes with 0 incoming edges so the ones
# that don't appear on [i,j] j.
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
smallest = findSmallestSetOfVertices(n,edges)
print(smallest)
