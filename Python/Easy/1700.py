
def countStudents(students, sandwiches):
    while sandwiches:
        if sandwiches[0] in students:
            students.remove(sandwiches[0])
            sandwiches.pop(0)
        else:
            break
    return len(sandwiches)
    # canEat = True
    # queue = []
    # while canEat:
    #     if not sandwiches:
    #         break
    #     elif not students:
    #         if queue[0] == sandwiches[0]:
    #             students = queue.copy()
    #             queue = []
    #             students.pop(0)
    #             sandwiches.pop(0)
    #         elif queue[0] in sandwiches:
    #             students = queue.copy()
    #             queue = []
    #         else:
    #             canEat = False
    #     elif students[0] == sandwiches[0]:
    #         students.pop(0)
    #         sandwiches.pop(0)
    #     elif students[0] != sandwiches[0]:
    #         queue.append(students[0])
    #         students.pop(0)
    # return len(queue)


# students = [1,1,0,0]
# sandwiches = [0,1,0,1]
students = [0,0,0,1,1,1,1,0,0,0]
sandwiches = [1,0,1,0,0,1,1,0,0,0]
count = countStudents(students,sandwiches)
print(count)
