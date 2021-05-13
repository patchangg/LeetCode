
def numRookCaptures(board):
    row = 0
    col = 0
    for i in range(len(board)):
        if "R" in board[i]:
            row = i
            for s in range(len(board[i])):
                if board[i][s] == "R":
                    col = s
            break
    captured = 0
    for n in range(col,-1,-1):
        if board[row][n] == "p":
            captured += 1
            break
        elif board[row][n] == "B":
            break
    for g in range(col,8,1):
        if board[row][g] == "p":
            captured += 1
            break
        elif board[row][g] == "B":
            break
    for f in range(row,-1,-1):
        if board[f][col] == "p":
            captured += 1
            break
        elif board[f][col] == "B":
            break
    for z in range(row,8,1):
        if board[z][col] == "p":
            captured += 1
            break
        elif board[z][col] == "B":
            break
    return captured


board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
number = numRookCaptures(board)
print(number)
