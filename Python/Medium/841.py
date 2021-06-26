
def canVisitAllRooms(rooms):
    dfs = [0]
    seen = set(dfs)
    while dfs:
        print(dfs)
        i = dfs.pop()
        for j in rooms[i]:
            if j not in seen:
                dfs.append(j)
                seen.add(j)
                if len(seen) == len(rooms): return True
    return len(seen) == len(rooms)

# Depth First Search so start at 0 and add the rooms into a set and append to defs
# Go until DFS is empty, if all rooms have been visted return True else False. O(N + E)
input = [[1,3],[3,0,1],[2],[0]]
canVisit = canVisitAllRooms(input)
print(canVisit)
