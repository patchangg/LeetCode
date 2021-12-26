
def checkIfPrerequisite(numCourses, prerequisites, queries):
    preReq = [[False] * numCourses for _ in range(numCourses)]

    for u, v in prerequisites:
        preReq[u][v] = True

    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                preReq[i][j] = preReq[i][j] or (preReq[i][k] and preReq[k][j])

    return [preReq[i][j] for i, j in queries]

# Change the Floyd-Warshall algorithm to check if each vertice is
# connected in the graph. O(n^3), O(n^2) space
numCourses = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]
isPrerequisite = checkIfPrerequisite(numCourses,prerequisites,queries)
print(isPrerequisite)
