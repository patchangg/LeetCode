
def networkDelayTime(times, n, k):
    dist = [float("inf") for _ in range(n)]
    dist[k-1] = 0
    for _ in range(n-1):
        for u, v, w in times:
            if dist[u-1] + w < dist[v-1]:
                dist[v-1] = dist[u-1] + w
    if max(dist) < float("inf"):
        return max(dist)
    else:
        return -1

# Use Bellman-Ford Algorithm to find the time to reach n nodes. If a node
# is unreachable, then return -1. O(V * E), O(n) space
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
timeToReachNNodes = networkDelayTime(times,n,k)
print(timeToReachNNodes)
