
def allPathsSourceTarget(graph):
    def dfs(cur, path):
        if cur == len(graph) - 1:
            result.append(path)
        else:
            for i in graph[cur]:
                dfs(i, path + [i])
    result = []
    dfs(0, [0])
    return result

graph = [[1,2],[3],[3],[]]
apst = allPathsSourceTarget(graph)
print(apst)
