
def findCircleNum(self, isConnected: List[List[int]]) -> int:
    seen = set()
    def dfs(node):
        for neighbour,adjacent in enumerate(isConnected[node]):
            if adjacent and neighbour not in seen:
                seen.add(neighbour)
                dfs(neighbour)
    output = 0
    for i in range(len(isConnected)):
        if i not in seen:
            dfs(i)
            output += 1
    return output

# Province is a group of cities that are indirect or directly connected
# and no other cities outside the group
# Use DFS to check if any cities are connected to each other
# if a city is neighbour to another, add it to seen
# This gets how many provinces there are in the array as
# if the city is not in seen, that means that it's not connected to the previous
# cities, being part of a new province.
# O(V+E), O(bm) space
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
provinces = findCircleNum(isConnected)
print(provinces)
