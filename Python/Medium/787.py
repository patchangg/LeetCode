
def findCheapestPrice(n, flights, src, dst, k):
    dp = [[float(inf) for j in range(n)] for i in range(k+2)]
    for i in range(k+2):
        dp[i][src] = 0
    for i in range(1,k+2):
        for f in flights:
            u = f[0]
            v = f[1]
            w = f[2]
            if dp[i-1][u] != float(inf):
                dp[i][v] = min(dp[i][v], dp[i-1][u] + w)
    if dp[k+1][dst] == float(inf):
        return -1
    else:
        return dp[k+1][dst]

# From the node after the source node, find the cheapest method of getting
# there from the previous node, do this for every node until the k node.
# This will create a path of cheapest nodes leading up to the kth node
# O(n+2k) where n is length of flights and k is the k stops, O(nk) space
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
cheapestFlight = findCheapestPrice(n,flights,src,dst,k)
print(cheapestFlight)
