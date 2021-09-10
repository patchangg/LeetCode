
def makeConnected(n, connections):
    if len(connections) < n - 1:
        return -1
    G = [set() for i in range(n)]
    for a,b in connections:
        G[a].add(b)
        G[b].add(a)
    seen = [0] * n

    def dfs(conn):
        if seen[conn]:
            return 0
        seen[conn] = 1
        for l in G[conn]:
            dfs(l)
        return 1

    output = 0
    for i in range(n):
        output += dfs(i)
    return output - 1

# There has to be atleast n-1 connections to connect all the computers
# We only need to count the amount of connected networks as if there is enough
# cables to connect all the computers we don't care where it comes from
# so the amount of operations = number of connected computers - 1
# O(connections), O(n) space
n = 4
connections = [[0,1],[0,2],[1,2]]
minChanges = makeConnected(n,connections)
print(minChanges)
