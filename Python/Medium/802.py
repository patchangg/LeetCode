
def eventualSafeNodes(graph):
    output = []
    visited = [-1] * len(graph)
    def dfs(i):
        visited[i] = 0
        for node in graph[i]:
            if visited[node] == 0 or (visited[node] == -1 and dfs(node)):
                return True
        visited[i] = 1
        output.append(i)
        return False
    for i in range(len(graph)):
        if visited[i] == -1:
            dfs(i)
    return sorted(output)

# Create a visited list which marks if the node has been visited or not
# Go through each node and mark them as 0 which means they have been looked at
# Go through all their connections and if you meet with the same node again,
# that means there is a cyclem, that they are unsafe.
# If you loop through all the nodes neighbours and they do not go back to
# themselves, they means they are safe and add them to the list.
# Sort the list and return it, O(nlogn), O(n) space
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
safeNodes = eventualSafeNodes(graph)
print(safeNodes)
