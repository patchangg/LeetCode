import collections

def maximalNetworkRank(n, roads):
    edges = collections.defaultdict(set)
    for a,b in roads:
        edges[a].add(b)
        edges[b].add(a)
    output = 0
    for i in range(n):
        for j in range(i+1,n):
            output = max(output, len(edges[i]) + len(edges[j]) - (i in edges[j]))
    return output

# Store the edges between two cities into a dictionary
# In a loop, find the two cities with the most amount of edges - the direct
# link between the two cities if there is as we would count the link twice
# if not removed. O(n^2), O(e) space
n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
maxRank = maximalNetworkRank(n,roads)
print(maxRank)
