
def memLeak(memory1, memory2):
    counter = 1
    while memory1 >= counter or memory2 >= counter:
        if memory1 >= memory2:
            memory1 -= counter
        else:
            memory2 -= counter
        counter += 1
    return [counter,memory1,memory2]

memory1 = 2
memory2 = 2
leakage = memLeak(memory1,memory2)
print(leakage)
