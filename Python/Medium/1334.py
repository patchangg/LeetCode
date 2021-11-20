
def findTheCity(n, edges, distanceThreshold):
    distance = [[float('inf')] * n for _ in range(n)]
    for f,t,w in edges:
        distance[f][t] = distance[t][f] = w
    for i in range(n):
        distance[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j],distance[k][j] + distance[i][k])
    output = {}
    for i in range(n):
        cityCount = 0
        for d in distance[i]:
            if (d <= distanceThreshold):
                cityCount += 1
        output[cityCount] = i
    return output[min(output)]

# Use Floyd-Warshall Algorithm to find the distance to each city for every city
# Loop through each city and find how many cities they can connect to with
# a distance less than or equal to the threshold. Update the dictionary's
# city count with the latest city with that number as we want to get the
# greatest city with that count. O(n^3), O(n^2) space
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
leastNeighboursCity = findTheCity(n,edges,distanceThreshold)
