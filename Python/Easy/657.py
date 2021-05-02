
def judgeCircle(moves):
    locationx = 0
    locationy = 0
    for move in moves:
        if move == "U":
            locationx += 1
        elif move == "D":
            locationx -= 1
        elif move == "R":
            locationy += 1
        elif move == "L":
            locationy -= 1
    if locationx == 0 and locationy == 0:
        return True
    else:
        return False

moves = "LDRRLRUULR"
origin = judgeCircle(moves)
print(origin)
