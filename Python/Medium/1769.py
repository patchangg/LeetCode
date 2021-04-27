
def minOperations(boxes):
    minOp = []
    loop = len(boxes)
    i = 0
    while i < loop:
        movement = 0
        s = 0
        while s < loop:
            if s != i and boxes[s] == "1":
                movement += abs(i-s)
            s += 1
        minOp.append(movement)
        i += 1
    return minOp


boxes = "001011"
minOp = minOperations(boxes)
print(minOp)
