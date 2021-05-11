
def allCellsDistOrder(R, C, r0, c0):
    output = []
    for r in range(R):
        for c in range(C):
            output.append([r,c])
    output.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
    return output

R = 3
C = 3
r0 = 0
c0 = 2
# R = 1
# C = 2
# r0 = 0
# c0 = 0
distance = allCellsDistOrder(R,C,r0,c0)
print(distance)
