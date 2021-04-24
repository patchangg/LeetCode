
def squareIsWhite(coordinates):
    dict = {"a":"black","b":"white","c":"black","d":"white","e":"black","f":"white","g":"black","h":"white"}
    if dict[coordinates[0]] == "black":
        if (int(coordinates[1]) % 2) == 0:
            return True
        else:
            return False
    else:
        if (int(coordinates[1]) % 2) == 0:
            return False
        else:
            return True

coordinates = "c7"
isWhite = squareIsWhite(coordinates)
print(isWhite)
