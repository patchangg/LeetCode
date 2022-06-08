
def minMovesToSeat(seats, students):
    output = 0
    seats = sorted(seats)
    students = sorted(students)
    for i in range(len(seats)):
        output += abs(students[i]-seats[i])
    return output

seats = [3,1,5]
students = [2,7,4]
minMoves = minMovesToSeat(seats,students)
print(minMoves)
