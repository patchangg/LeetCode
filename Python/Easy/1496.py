
def isPathCrossing(self, path: str) -> bool:
    cords = [[0,0]]
    curr = [0,0]
    for p in path:
        if p == "N":
            curr[0] += 1
        elif p == "S":
            curr[0] -= 1
        elif p == "E":
            curr[1] += 1
        else:
            curr[1] -= 1
        if curr in cords:
            return True
        else:
            cords.append(curr[:])
    return False

path = "NES"
doesPathCross = isPathCrossing(path)
print(doesPathCross)
