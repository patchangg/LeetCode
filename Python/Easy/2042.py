
def areNumbersAscending(s):
    s = s.split(" ")
    numbers = [-1]
    for word in s:
        if word.isnumeric():
            if int(word) > numbers[-1]:
                numbers.append(int(word))
            else:
                return False
    return True

s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
isAscending = areNumbersAscending(s)
print(isAscending)
