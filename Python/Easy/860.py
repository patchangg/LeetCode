
def lemonadeChange(bills):
    fives = 0
    tens = 0

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            fives -= 1
            tens += 1
        elif tens > 0:
            fives -= 1
            tens -= 1
        else:
            fives -= 3
        if fives < 0:
            return False

bills = [5,5,5,10,20]
enoughChange = lemonadeChange(bills)
print(enoughChange)
